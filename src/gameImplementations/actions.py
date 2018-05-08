
from ..MillsGame import Phase

def actions(game, state):

    if state.to_move == 'W' and state.w_no_board != 0:
        Phase = 1
        return state.moves

    if state.to_move == 'B' and state.b_no_board != 0:
        Phase = 1
        return state.moves

    Phase = 0
