from .. import MillsGame

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

    moves = []

    if state.w_board == 0 and state.b_board == 0:
        return [4]

    possible_moves = state.moves
    possible_eliminate = MillsGame.can_eliminate(game, state)

    for move in possible_moves:
        moves.append(move, evaluate_single_move_phase1())

    if state.w_board < 3 and state.b_board < 3:
        # TODO Ancora non è possibile fare dei tris come ci comportiamo?
        print()
    else:
        # TODO fare la will_tris per scegliere la casella migliore
        print()
    return moves


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
    moves = MillsGame.can_move(game, state)
    return moves


def filter_phase3(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 3
    ( con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    moves = []
    return moves
