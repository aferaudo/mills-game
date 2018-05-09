
from .. import MillsGame


def actions(game, state):

    moves = state.moves
    player = state.to_move

    if game.Phase == 1:
        if state.w_board == 0 and state.b_board == 0:
            # Se è la prima mossa facciamo solo una di queste 4 (si potrebbe anche mandarne una sola)
            return [4, 10, 13, 19]

    if game.Phase == 2:
        # Prendo le mie pedine e direttamente metto nelle moves solo le possibili moves che sono adiacenti alle mie
        # Il for potrebbe essere ottimizzato o quantomeno reso in line
        moves = []
        for index, value in enumerate(state.board):
            if value == player:
                moves.extend(MillsGame.adjacent_locations(index))

        moves = list(set(moves))  # set serve per rimuovere i duplicati
        # Prendo le pedine dell'avversario per toglierle tra le moves che sto restituendo
        other_player_pieces = game.player_pieces(state, ('W' if player == 'B' else 'B'))
        return list(set(moves) - set(other_player_pieces))

    return moves
