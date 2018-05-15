from .. import MillsGame
from ..game_utils import *

"""This file contains the heuristics of the game
For example:
Heuristic that looks at the number of pieces and the potential mills
that could be formed

This function (eval_fun) return a value that can be used by alpha beta algotithm
"""


def evaluate_single_move_phase1(game, state, move):
    print()


def filter_phase1(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 1
    (con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    adjacent_weight = 1
    couple = 2
    tris_weight = 7
    block_tris = 6
    double_game = 4
    block_double_game = 5
    block_piece = 1

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

        # aggiungo la mossa alle mosse da restituire
        moves.append(tuple((move, value)))

    moves = sorted(moves, key=lambda x: x[1])
    moves = moves[len(moves)-num_moves_to_return:len(moves)]
    moves.reverse()

    moves_to_return = []
    for move in moves:
        has_to_delete = check_tris(state.board, -1, move, player)
        moves_to_return.append(tuple((-1, move[0], 1 if has_to_delete else 0)))

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
    moves = MillsGame.can_move(state)
    return moves


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
