from ..game_utils import *
"""Contiene l'euristica per la scelta della pedina da eliminare"""


def delete_pieces_phase1(state):
    """
    con questa funzione prendiamo uno stato e a partire da tutte le possibili pedine avversarie
    eliminabili scegliamo quella da eliminare più conveniente fase 1
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
    mine_tris = check_tris_on_board(state)

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
        check_couples_num = check_couples(state, move, opponent, True)
        if check_couples_num == 2:
            value += check_couples_num * double_game_opponent
        else:
            value += check_couples_num * couple_opponent

        # valuto se l'avversario blocca un doppio gioco
        check_double_occupied = check_couples(state, move, player)
        if check_double_occupied == 2:
            value += check_double_occupied * double_game_player

        # valuto se questa pedina blocca un mio tris
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

    deletable = sorted(deletable, key=lambda x: (-x[1], x[0]))

    return deletable[0] if len(deletable) > 0 else state.moves


def delete_pieces_phase2(state):
    """
    con questa funzione prendiamo uno stato e a partire da tutte le possibili pedine avversarie
    eliminabili scegliamo quella da eliminare più conveniente fase 2
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
    mine_tris = check_tris_on_board(state)

    # controlliamo in che fase è l'avversario
    if (opponent == "B" and state.b_board == 3) or (opponent == "W" and state.w_board == 3):
        # se l'avversario è in fase 3 restituisco la prima pedina da eliminare
        return tuple((deletable_pieces[0], 0))

    for piece in deletable_pieces:
        # inizialmente non ho vantaggi con questa mossa
        value = 0

        # valutiamo se la la pedina dell'avversario ci blocca un tris
        if check_tris(state.board, -1, piece, player):
            value += tris_weight

        # valuto se l'avversario ha un doppio gioco o una coppia
        check_couples_list = check_couples_future_tris_delete(state, piece, opponent)
        if len(check_couples_list) == 2:
            value += len(check_couples_list) * double_game_opponent
        else:
            value += len(check_couples_list) * couple_opponent

        # valuto se gli adiacenti delle coppie contengono una pedina che gli permette di fare tris
        num_future_tris = check_future_tris(check_couples_list, state.board, opponent)
        value += num_future_tris * tris_weight

        # valuto se l'avversario blocca un doppio gioco
        check_double_occupied = check_couples(state, piece, player)
        if check_double_occupied == 2:
            value += check_double_occupied * double_game_player

        # valuto se questa pedina blocca un mio tris
        for tris in mine_tris:
            its_adjacents = tris_adjacents(tris)
            if piece in its_adjacents:
                check = len(its_adjacents)
                for x in its_adjacents:
                    if state.board[x] != 'O':
                        check -= 1
                if check == 0:
                    value += blocking_tris_weight

        deletable.append(tuple((piece, value)))

    deletable = sorted(deletable, key=lambda x: (-x[1], x[0]))

    return deletable[0] if len(deletable) > 0 else state.moves


def delete_pieces_phase3(state):
    """
    con questa funzione prendiamo uno stato e a partire da tutte le possibili pedine avversarie
    eliminabili scegliamo quella da eliminare più conveniente fase 2
    :param state:
    :return:
    """

    couple_opponent = 2
    tris_weight = 7
    double_game_opponent = 4

    player = state.to_move
    opponent = "B" if player == "W" else "W"

    deletable = []
    deletable_pieces = can_eliminate(state)
    mine_tris = check_tris_on_board(state)

    # controlliamo in che fase è l'avversario
    if (opponent == "B" and state.b_board == 3) or (opponent == "W" and state.w_board == 3):
        # se anche l'avversario è in fase 3 restituisco la prima eliminabile
        return tuple((deletable_pieces[0], 0))

    for piece in deletable_pieces:
        # inizialmente non ho vantaggi con questa mossa
        value = 0

        # valuto se l'avversario ha un doppio gioco o una coppia
        check_couples_list = check_couples_future_tris_delete(state, piece, opponent)
        if len(check_couples_list) == 2:
            value += len(check_couples_list) * double_game_opponent
        else:
            value += len(check_couples_list) * couple_opponent

        # valuto se gli adiacenti delle coppie contengono una pedina che gli permette di fare tris
        num_future_tris = check_future_tris(check_couples_list, state.board, opponent)
        value += num_future_tris * tris_weight

        deletable.append(tuple((piece, value)))

    deletable = sorted(deletable, key=lambda x: (-x[1], x[0]))

    return deletable[0] if len(deletable) > 0 else state.moves
