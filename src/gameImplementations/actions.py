
from .. import MillsGame


def actions(game, state):

    if state.to_move == 'W' and state.w_no_board != 0:
        game.Phase = 1
        return state.moves

    if state.to_move == 'B' and state.b_no_board != 0:
        game.Phase = 1
        return state.moves

    game.Phase = 0
