
from .. import MillsGame


def actions(game, state):

    if MillsGame.Phase == 1:
        if state.w_board == 0 and state.b_board == 0:
            return state.moves
    return state.moves
