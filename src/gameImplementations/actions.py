
from .. import MillsGame


def actions(game, state):

    if MillsGame.Phase == 1:
        if state.w_board == 0 and state.b_board == 0:
            return [4, 10, 13, 19]
    return state.moves
