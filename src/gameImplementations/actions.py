
from .. import MillsGame


def opponent_will_tris(game, state):
    opponent = "W" if state.to_move == "B" else "B"
    opponent_pieces = game.player_pieces(game, state, opponent)
    hot_position = []  # conterrà tutte le posizioni della board in cui l'avversario hai dei tris aperi
    for index in opponent_pieces:
        print(MillsGame.check_tris(state, index))
        # TODO da finire



def actions(game, state):

    moves = state.moves
    player = state.to_move

    if game.Phase == 1:
        if state.w_board == 0 and state.b_board == 0:
            # Se è la prima mossa facciamo solo una di queste 4 (si potrebbe anche mandarne una sola)
            return [4]
        # TODO Manca tutta la logica vera della phase 1

    if game.Phase == 2:
        # Prendo le mie pedine e direttamente metto nelle moves solo le possibili moves che sono adiacenti alle mie
        # Il for potrebbe essere ottimizzato o quantomeno reso in line

        return MillsGame.can_move(game, state, player)

    return moves
