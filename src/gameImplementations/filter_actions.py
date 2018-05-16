from .. import MillsGame
from ..game_utils import *
from .delete_strategy import *

"""This file contains the heuristics of the game
For example:
Heuristic that looks at the number of pieces and the potential mills
that could be formed

This function (eval_fun) return a value that can be used by alpha beta algotithm
"""


def filter_phase1(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 1
    (con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    # TODO Controllare pesi (da fare alla fine)
    adjacent_weight = 1
    couple = 2
    tris_weight = 7
    block_tris = 6
    double_game = 4
    block_double_game = 5
    block_piece_weight = 1.5
    mine_block_piece_weight = -1

    num_moves_to_return = 5

    player = state.to_move
    opponent = "B" if player == "W" else "W"

    moves = []

    if state.w_board == 0 and state.b_board == 0:
        return [tuple((-1, 4, -1))]

    possible_moves = state.moves

    for move in possible_moves:
        # inizialmente non ho vantaggi con questa mossa
        value = 0

        # qua calcoliamo quanti adiacenti liberi ha la mossa corrente
        adjacent = adjacent_locations(move)
        adjacent = remove_moves_occupied(state, adjacent)
        value += len(adjacent) * adjacent_weight

        # valutiamo se la mosse corrente ci porta a fare un tris
        if check_tris(state.board, -1, move, player):
            value += tris_weight

        # valuto se blocco un futuro tris dell'avversario
        if check_tris(state.board, -1, move, opponent):
            value += block_tris

        # valuto se facciamo un doppio gioco o coppia
        check_couples_num = check_couples(state, move, player)
        if check_couples_num == 2:
            value += check_couples_num * double_game
        else:
            value += check_couples_num * couple

        # valuto se blocchiamo un doppio gioco
        if check_double_game(state, move, opponent):
            value += block_double_game

        # valuto se blocco delle pedine avversarie
        pieces_blocked = block_pieces(state, move, player)
        value += pieces_blocked * block_piece_weight

        # valuto se blocco delle mie pedine (in questo caso la mossa sarà PENALIZZATA)
        mine_pieces_blocked = block_pieces(state, move, opponent)
        value += mine_pieces_blocked * mine_block_piece_weight

        # aggiungo la mossa alle mosse da restituire
        moves.append(tuple((move, value)))

    moves = sorted(moves, key=lambda x: x[1])
    moves = moves[len(moves)-num_moves_to_return:len(moves)]
    moves.reverse()

    moves_to_return = []
    for move in moves:
        has_to_delete = check_tris(state.board, -1, move[0], player)
        # print(has_to_delete)
        if has_to_delete:
            to_delete = delete_pieces_phase1(state)
            # print(has_to_delete, to_delete)

        moves_to_return.append(tuple((-1, move[0], to_delete[0] if has_to_delete else -1)))

    return moves_to_return if len(moves_to_return) > 0 else state.moves


def filter_phase2(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 2
    ( con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    # TODO Sommare euristica eliminazione pedina
    moves = []

    # TODO Controllare pesi (da fare alla fine)
    player_will_tris = 10
    player_tris_trick = 7
    player_couple = 2
    player_double_game = 5
    opponent_will_tris = -7
    opponent_tris_will_unlock = -5


    num_moves_to_return = 5

    player = state.to_move
    opponent = "B" if player == "W" else "W"

    possible_moves = can_move(state, player)

    all_board_tris = all_tris_on_board(state)
    player_tris = all_board_tris[player]
    opponent_tris = all_board_tris[opponent]

    for move in possible_moves:
        # TODO probabilmente dovremo controllare anche altri aspetti
        # inizialmente non ho vantaggi con questa mossa
        value = 0

        # valutare se facendo questa mossa consento all'avversario di fare un tris (punteggio negativo)
        # è caso molto raro non so se serve farlo
        # per farlo dobbiamo vedere se move[0] sta nella can_move dell'opponent e poi vedere se
        # check_tris(state.board, -1, move[0], opponent) restituisce True, in quel caso non mi devo muovere

        # valuto se muovendomi faccio un tris
        if check_tris(state.board, move[0], move[1], player):
            value += player_will_tris

        # valutare se facendo questa mossa libero una tris bloccato avversario (punteggio negativo)
        if unlock_opponent_tris(opponent_tris, move[0]):
            value += opponent_tris_will_unlock

        # valutare se muovendomi creo una coppia o un doppio gioco
        # TODO valutare se può essere intelligente considerare come coppia favorevole se la terza pedina della coppia è occupata dall'avversario
        # TODO non funziona bene questo check
        check_couples_num = check_couples_phase_two(state, move[0], move[1], player)
        if check_couples_num == 2:
            value += check_couples_num * player_double_game  # gli do un valore basso il doppio gioco è importante nella fase 1, meno nella 2
        else:
            value += check_couples_num * player_couple

        # se ho fatto un tris e posso fare il trick di fare tris ogni due mosse
        if move_in_player_tris(player_tris, move[0]):
            value += player_tris_trick

        # aggiungo la mossa alla lista
        moves.append(tuple((move[0], move[1], value)))

    # alla fine ordinare le mosse sencondo il value in maniere decrescente e poi se il numero di mosse è sotto una
    # certa soglia le restituisco tutte altrimenti taglio solo ad N mosse

    moves = sorted(moves, key=lambda x: (-x[2], x[1], x[0]))
    print("moves after order = " + str(moves))
    if len(moves) > num_moves_to_return:
        moves = moves[0:num_moves_to_return]

    moves_to_return = []
    for move in moves:
        has_to_delete = check_tris(state.board, move[0], move[1], player)
        if has_to_delete:
            to_delete = delete_pieces_phase2(state)
            print("To delete = " + str(to_delete))

        moves_to_return.append(tuple((move[0], move[1], to_delete[0] if has_to_delete else -1)))

    return moves_to_return if len(moves_to_return) > 0 else possible_moves


def filter_phase3(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 3
    ( con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    moves = state.moves
    return moves
