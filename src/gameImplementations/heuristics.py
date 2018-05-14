from .. import MillsGame

"""This file contains the heuristics of the game
For example:
Heuristic that looks at the number of pieces and the potential mills
that could be formed

This function (eval_fun) return a value that can be used by alpha beta algotithm
"""


def heuristic_phase1(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 1
    ( con punteggio più alto)
    :param game:
    :param state:
    :return:
    """
    moves = []

    if state.w_board == 0 and state.b_board == 0:
        return [4]
    elif state.w_board < 3 and state.b_board < 3:
        # TODO Ancora non è possibile fare dei tris come ci comportiamo?
        print()
    else:
        # TODO fare la will_tris per scegliere la casella migliore
        print()

    return moves


def heuristic_phase2(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 2
    ( con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    moves = []
    moves = MillsGame.can_move(game, state)
    return moves


def heuristic_phase3(game, state):
    """
    questa funzione prende in ingresso lo stato e restutuisce le mosse migliori per la fase 3
    ( con punteggio più alto)
    :param game:
    :param state:
    :return:
    """

    moves = []
    return moves
