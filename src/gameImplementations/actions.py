
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
            return [4]
        elif state.w_board < 3 and state.b_board < 3:
            # TODO Ancora non è possibile fare dei tris come ci comportiamo?
            print()
        else:
            # TODO fare la will_tris per scegliere la casella migliore
            print()

    if game.Phase == 2:
        # Prendo le mie pedine e direttamente metto nelle moves solo le possibili moves che sono adiacenti alle mie
        # Il for potrebbe essere ottimizzato o quantomeno reso in line

        return MillsGame.can_move(game, state, player)

    return moves
