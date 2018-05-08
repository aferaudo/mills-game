

def utility(game, state, player):
    """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
    return state.utility if player == 'W' else -state.utility