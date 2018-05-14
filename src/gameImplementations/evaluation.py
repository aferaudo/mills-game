"""Contiene le funzioni che valutano la probabilità di vittoria arrivati in un certo stato"""

from ..MillsGame import *
from ..game_utils import *


def eval_fun_phase1(state):
    """
    Restituisce una valutazione sulla vittoria secondo la board corrente (State)
    :param state:
    :return:
    """
    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra i tris miei e quelli dell'avversario
    num_tris_now = len(check_tris_on_board(state, player))
    num_tris_next = len(check_tris_on_board(state, opponent))
    evaluation = (num_tris_now - num_tris_next)

    #print(evaluation)

    return evaluation


def eval_fun_phase2(state):
    player = state.to_move
    return state.utility if player == 'W' else -state.utility


def eval_fun_phase3(state):
    print()
