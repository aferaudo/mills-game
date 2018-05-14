
from .heuristics import *
from .. import MillsGame


def opponent_will_tris(game, state):
    opponent = "W" if state.to_move == "B" else "B"
    opponent_pieces = game.player_pieces(game, state, opponent)
    hot_position = []  # conterrà tutte le posizioni della board in cui l'avversario hai dei tris aperi
    for index in opponent_pieces:
        print(MillsGame.check_tris(state, index))
        # TODO da finire


def actions(game, state):
    """
    prende in ingresso lo stato corrente (disposizione pedine sulla board) e restituisce
    le azioni fattibili dal giocatore che sta muovendo in base alla fase di gioco corrente
    fase 1: disposizione iniziale delle pedine sulla board
    fase 2: movimento pedine sulla board da una posizione ad una adiacente
    fase 3: movimento pedine sulla board da una posizione ad un'altra qualsiasi
    :param game:
    :param state:
    :return:
    """

    moves = state.moves
    player = state.to_move

    if game.Phase == 1:
        moves = heuristic_phase1(game, state)

    if game.Phase == 2:
        moves = heuristic_phase2(game, state)

    if game.Phase == 3:
        moves = heuristic_phase3(game, state)
    return moves
