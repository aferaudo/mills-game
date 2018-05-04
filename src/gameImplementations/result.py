
from collections import namedtuple

GameState = namedtuple('GameState', 'to_move, utility, board, moves')


def result(game, state, move):
    return GameState(to_move='O', utility=0, board={}, moves=move)
