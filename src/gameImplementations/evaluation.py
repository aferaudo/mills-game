"""Contiene le funzioni che valutano la probabilità di vittoria arrivati in un certo stato"""

from ..MillsGame import *
from ..game_utils import *
from .result import compute_utility


def eval_fn_stupid(state):
    """
    La primixima funxione bellixima
    :param state:
    :return:
    """
    victory = state.utility
    w_pieces = state.w_board + state.w_no_board
    b_pieces = state.b_board + state.b_no_board
    if state.to_move == 'W':
        value = w_pieces-b_pieces
        return value + victory
    else:
        value = b_pieces - w_pieces
        return value + victory


def eval_fn_num_pieces(state, weight):
    """
    Valuta la differenza di pedine tra i due giocatori
    :param state:
    :return:
    """

    w_pieces = state.w_board + state.w_no_board
    b_pieces = state.b_board + state.b_no_board
    if state.to_move == 'W':
        return (w_pieces - b_pieces) * weight
    else:
        return (b_pieces - w_pieces) * weight


def eval_fn_num_tris(state, weight):
    """
    Valuta la differenza tra il numero di tris dei due giocatori
    :param state:
    :param weight:
    :return:
    """
    all_tris = all_tris_on_board(state)
    if state.to_move == 'W':
        return (len(all_tris['W']) - len(all_tris['B'])) * weight
    else:
        return (len(all_tris['B']) - len(all_tris['W'])) * weight


def eval_fn_num_adjacents(state, weight):
    """
    Valuta la differenza tra il numero di adiacenti dei giocatori
    :param state:
    :param weight:
    :return:
    """
    board = state.board
    all_pieces = all_pieces_on_board_for_each_player(state)
    adjacents_w = count_all_adjacents_player(board, all_pieces['W'])
    adjacents_b = count_all_adjacents_player(board, all_pieces['B'])

    if state.to_move == 'W':
        return (adjacents_w - adjacents_b) * weight
    else:
        return (adjacents_b - adjacents_w) * weight


def eval_fn_smart(state):
    """
    È la nostra eval generica che in base alla fase sceglie quale funzione usare per valutare lo stato
    :param state:
    :return:
    """
    # implementare con diverse fasi

    player = state.to_move
    phase = check_phase(state.w_no_board, state.b_no_board, state.w_board, state.b_board, player)

    victory = state.utility

    if phase == 1:
        return eval_fn_phase1(state) + victory
    if phase == 2:
        return eval_fn_phase2(state) + victory
    if phase == 3:
        return eval_fn_phase3(state) + victory


def eval_fn_phase1(state):
    """
    Restituisce una valutazione sulla vittoria secondo la board corrente (State)
    :param state:
    :return:
    """

    # pesi per le sub eval
    num_pieces_weight = 100
    num_adjacents_weight = 1
    num_tris_weight = 5

    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra le pedine dei giocatori
    evaluation += eval_fn_num_pieces(state, num_pieces_weight)

    # calcoliamo la differenza tra gli adiacenti dei giocatori
    # evaluation += eval_fn_num_adjacents(state, num_adjacents_weight)

    # calcoliamo la differenza tra il numero di tris dei giocatori
    evaluation += eval_fn_num_tris(state, num_tris_weight)

    #print(evaluation)

    return evaluation


def eval_fn_phase2(state):
    """
        Restituisce una valutazione sulla vittoria secondo la board corrente (State)
        :param state:
        :return:
        """

    # pesi per le sub eval
    num_pieces_weight = 100
    num_adjacents_weight = 2
    num_tris_weight = 3

    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra le pedine dei giocatori
    evaluation += eval_fn_num_pieces(state, num_pieces_weight)

    # calcoliamo la differenza tra gli adiacenti dei giocatori
    # evaluation += eval_fn_num_adjacents(state, num_adjacents_weight)

    # calcoliamo la differenza tra il numero di tris dei giocatori
    evaluation += eval_fn_num_tris(state, num_tris_weight)

    # print(evaluation)

    return evaluation


def eval_fn_phase3(state):
    """
        Restituisce una valutazione sulla vittoria secondo la board corrente (State)
        :param state:
        :return:
        """

    # pesi per le sub eval
    num_pieces_weight = 1
    num_adjacents_weight = 0
    num_tris_weight = 3

    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra le pedine dei giocatori
    evaluation += eval_fn_num_pieces(state, num_pieces_weight)

    # calcoliamo la differenza tra gli adiacenti dei giocatori
    # evaluation += eval_fn_num_adjacents(state, num_adjacents_weight)

    # calcoliamo la differenza tra il numero di tris dei giocatori
    evaluation += eval_fn_num_tris(state, num_tris_weight)

    # print(evaluation)

    return evaluation


def eval_fn_opponent(state):
    """
    È la nostra eval generica che in base alla fase sceglie quale funzione usare per valutare lo stato
    :param state:
    :return:
    """

    player = state.to_move
    phase = check_phase(state.w_no_board, state.b_no_board, state.w_board, state.b_board, player)

    victory = state.utility

    if phase == 1:
        return eval_fn_phase1_opponent(state) + victory
    if phase == 2:
        return eval_fn_phase2_opponent(state) + victory
    if phase == 3:
        return eval_fn_phase3_opponent(state) + victory


def eval_fn_phase1_opponent(state):
    """
    Restituisce una valutazione sulla vittoria secondo la board corrente (State)
    :param state:
    :return:
    """

    # pesi per le sub eval
    num_pieces_weight = 1
    num_adjacents_weight = 1
    num_tris_weight = 3

    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra le pedine dei giocatori
    evaluation += eval_fn_num_pieces(state, num_pieces_weight)

    # calcoliamo la differenza tra il numero di tris dei giocatori
    evaluation += eval_fn_num_tris(state, num_tris_weight)

    #print(evaluation)

    return evaluation


def eval_fn_phase2_opponent(state):
    """
        Restituisce una valutazione sulla vittoria secondo la board corrente (State)
        :param state:
        :return:
        """

    # pesi per le sub eval
    num_pieces_weight = 10
    num_adjacents_weight = 1
    num_tris_weight = 3

    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra le pedine dei giocatori
    evaluation += eval_fn_num_pieces(state, num_pieces_weight)

    # calcoliamo la differenza tra il numero di tris dei giocatori
    evaluation += eval_fn_num_tris(state, num_tris_weight)

    # print(evaluation)

    return evaluation


def eval_fn_phase3_opponent(state):
    """
        Restituisce una valutazione sulla vittoria secondo la board corrente (State)
        :param state:
        :return:
        """

    # pesi per le sub eval
    num_pieces_weight = 1
    num_adjacents_weight = 1
    num_tris_weight = 3

    player = state.to_move
    opponent = "B" if player == "W" else "W"
    evaluation = 0

    # Stiamo calcolando la differenza tra le pedine dei giocatori
    evaluation += eval_fn_num_pieces(state, num_pieces_weight)

    # calcoliamo la differenza tra il numero di tris dei giocatori
    evaluation += eval_fn_num_tris(state, num_tris_weight)

    # print(evaluation)

    return evaluation