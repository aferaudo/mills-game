
def terminal_test(game, state):
    """A state is terminal if it is won or there are no empty squares."""
    return state.utility != 0 or len(state.moves) == 0
