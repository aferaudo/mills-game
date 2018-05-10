
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
    new_state = None

    # Check phase
    if state.w_no_board == 0 and state.b_no_board == 0:
        game.Phase = 2

    if game.Phase == 1:
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        new_state = GameState(to_move=('B' if state.to_move == 'W' else 'W'),
                              utility=compute_utility(game, state),
                              board=board,
                              moves=moves,
                              w_board=(state.w_board + 1 if state.to_move == 'W' else state.w_board),
                              b_board=(state.b_board + 1 if state.to_move == 'B' else state.b_board),
                              w_no_board=(state.w_no_board - 1 if state.to_move == 'W' else state.w_no_board),
                              b_no_board=(state.b_no_board - 1 if state.to_move == 'B' else state.b_no_board)
                              )
    elif game.Phase == 2:
        print()
        # TODO prima dobbiamo modificare la can_move

    # Prima di fare il return del nuovo stato è necessario calcolare la phase,
    # perchè al termine della result la phase deve essere già a due se con questo mossa entriamo nella seconda phase

    if new_state.w_no_board == 0 and new_state.b_no_board == 0:
        game.Phase = 2

    return new_state


def compute_utility(game, state):
    """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0.
    É provvisoria solo per la fase 1
    """
    if game.Phase == 1:
        if state.w_no_board == 0 and state.b_no_board == 0:
            return 1 if state.to_move == 'W' else -1
        else:
            return 0

    else:
        if state.to_move == 'W' and state.b_no_board == 0 and state.b_board == 0:
            return 1
        elif state.to_move == 'B' and state.w_no_board == 0 and state.w_board == 0:
            return -1
        else:
            return 0
