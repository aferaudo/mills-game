
from collections import namedtuple
from ..game_utils import check_phase, can_move
from .delete_strategy import *
from .. import MillsGame
"""
Game State
to_move = rappresenta di chi è il turno corrente
utility = 1 con la prossima mossa vinciamo, -1 perdiamo, 0 non succede
board = rappresentazione della board
moves = possibili mosse a partire dallo stato corrente
w_board = pedine bianche sulla board
b_board = pedine nere sulla board
w_no_board = pedine bianche ancora da mettere in gioco
b_no_board = pedine nere ancora da mettere in gioco
"""
GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')


def result(game, state, move):
    """
    Prende in ingresso lo stato della board e la mossa fatta, controllando se è valida.
    :param game:
    :param state:
    :param move:
    :return: new_state
    """
    if move[1] not in state.moves:
        return state  # Illegal move has no effect

    board = state.board.copy()
    moves = list(state.moves)
    next_player = ('B' if state.to_move == 'W' else 'W')
    board[move[1]] = state.to_move

    # aggiorno la board eseguendo il movimento/schieramento presente in move
    if move[0] == -1:
        moves.remove(move[1])
        new_w_board = state.w_board + 1 if state.to_move == 'W' else state.w_board
        new_b_board = state.b_board + 1 if state.to_move == 'B' else state.b_board
        w_no_board = state.w_no_board - 1 if state.to_move == 'W' else state.w_no_board
        b_no_board = state.b_no_board - 1 if state.to_move == 'B' else state.b_no_board
    else:
        board[move[0]] = 'O'
        moves[moves.index(move[1])] = move[0]
        new_w_board = state.w_board
        new_b_board = state.b_board
        w_no_board = 0
        b_no_board = 0

    # controllo se devo eliminare la pedina avversaria
    if move[2] != -1:
        board[move[2]] = 'O'
        moves.append(move[2])
        if state.to_move == 'B':
            new_w_board = state.w_board - 1
        else:
            new_b_board = state.b_board - 1

    return GameState(to_move=next_player,
                     utility=compute_utility(state, w_no_board, b_no_board, new_w_board, new_b_board),
                     board=board,
                     moves=moves,
                     w_board=new_w_board,
                     b_board=new_b_board,
                     w_no_board=w_no_board,
                     b_no_board=b_no_board
                     )


def compute_utility(state, w_no_board, b_no_board, w_board, b_board):
    """If 'W' wins with this move, return 1; if 'B' wins return -1; else return 0.
    É provvisoria solo per la fase 1
    """
    victory_value = 1000
    if check_phase(w_no_board, b_no_board, w_board, b_board, state.to_move) == 1:
        # TODO Why?
        if w_no_board == 0 and b_no_board == 0:
            return victory_value if state.to_move == 'W' else -victory_value
        else:
            return 0

    else:
        if state.to_move == 'W' and (b_board == 2 or len(can_move(state, 'B')) == 0):
            return victory_value
        elif state.to_move == 'B' and (w_board == 2 or len(can_move(state, 'W')) == 0):
            return -victory_value
        else:
            return 0
