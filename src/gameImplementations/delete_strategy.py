from ..game_utils import *
"""Contiene l'euristica per la scelta della pedina da eliminare"""


def delete_pieces_phase1(state):
    """
    con questa funzione prendiamo uno stato e a partire da tutte le possibili pedine avversarie
    eliminabili scegliamo quella da eliminare più conveniente
    :param game:
    :param state:
    :return:
    """

    adjacent_weight = 1
    couple_opponent = 2
    tris_weight = 7
    double_game_opponent = 4
    double_game_player = 3
    blocking_weight = 1

    num_deletable_to_remove = 1

    player = state.to_move
    opponent = "B" if player == "W" else "W"

    deletable = []
    deletable_pieces = can_eliminate(state)

    for move in deletable_pieces:
        # inizialmente non ho vantaggi con questa mossa
        value = 0

        # qua calcoliamo quanti adiacenti liberi ha la pedina dell'avversario
        adjacent = adjacent_locations(move)
        adjacent = remove_moves_occupied(state, adjacent)
        value += len(adjacent) * adjacent_weight

        # valutiamo se la la pedina dell'avversario ci blocca un tris
        if check_tris(state.board, -1, move, player):
            value += tris_weight

        # valuto se l'avversario ha un doppio gioco o una coppia
        check_couples_num = check_couples(state, move, opponent)
        if check_couples_num == 2:
            value += check_couples_num * double_game_opponent
        else:
            value += check_couples_num * couple_opponent

        # valuto se l'avversario blocca un doppio gioco
        check_double_occupied = check_couples(state, move, player)
        if check_double_occupied == 2:
            value += check_double_occupied * double_game_player

        # valuto se questa pedina blocca un mio tris
        # total_blocking = 0
        # player_tris = check_tris_on_board(state, player)
        # for tris in player_tris:
        #     for piece in tris:
        #         if piece in locations()[move]: # TODO cambia come blocco non basta che sia adiacente
        #             total_blocking += blocking_weight
        # value += total_blocking

        deletable.append(tuple((move, value)))

    deletable = sorted(deletable, key=lambda x: x[1])

    return deletable[len(deletable)-1] if len(deletable) > 0 else state.moves
