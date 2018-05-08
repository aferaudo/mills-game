
from collections import namedtuple
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
    if move not in state.moves:
        return state  # Illegal move has no effect
    board = state.board.copy()
    board[move] = state.to_move
    moves = list(state.moves)
    moves.remove(move)
    # Check phase
    if state.w_no_board == 0 and state.b_no_board == 0:
        MillsGame.Phase = 2

    if MillsGame.Phase == 1:
        return GameState(to_move=('B' if state.to_move == 'W' else 'W'),
                         utility=0,
                         board=board,
                         moves=moves,
                         w_board=(state.w_board+1 if state.to_move == 'W' else state.w_board),
                         b_board=(state.b_board+1 if state.to_move == 'B' else state.b_board),
                         w_no_board=(state.w_no_board-1 if state.to_move == 'W' else state.w_no_board),
                         b_no_board=(state.b_no_board-1 if state.to_move == 'B' else state.b_no_board)
                         )

    return None