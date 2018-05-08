
from collections import namedtuple
from ..MillsGame import GameState


def result(game, state, move):
    if move not in state.moves:
        return state  # Illegal move has no effect
    board = state.board.copy()
    board[move] = state.to_move
    moves = list(state.moves)
    moves.remove(move)
    return GameState(to_move=('W' if state.to_move == 'B' else 'W'),
                     utility=game.compute_utility(board, move, state.to_move),
                     board=board,
                     moves=moves
                     )
