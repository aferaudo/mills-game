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
    blocking_tris_weight = 5

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

        # TODO provare se questa vualutazione funziona
        # valuto se questa pedina blocca un mio tris
        mine_tris = check_tris_on_board(state)
        for tris in mine_tris:
            its_adjacents = tris_adjacents(tris)
            if move in its_adjacents:
                check = len(its_adjacents)
                for x in its_adjacents:
                    if state.board[x] != 'O':
                        check -= 1
                if check == 0:
                    value += blocking_tris_weight

        deletable.append(tuple((move, value)))

    deletable = sorted(deletable, key=lambda x: x[1])

    return deletable[len(deletable)-1] if len(deletable) > 0 else state.moves
