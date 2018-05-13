
from collections import namedtuple
from .. import MillsGame
"""
Game State
to_move = rappresenta di chi è il turno corrente
utility = 1 con la prossima mossa vinciamo, -1 perdiamo, 0 non succede
board = rappresentazione della board
moves = possibili mosse a partire dallo stato corrente
w_board = pedine bianche sulla board
b_board = pedine nere sulla board
w_no_board = pedine bianche ancora da mettere in gioco
b_no_board = pedine nere ancora da mettere in gioco
"""
GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')


def result(game, state, move):
    """
    Prende in ingresso lo stato della board e la mossa fatta, controllando se è valida.
    :param game:
    :param state:
    :param move:
    :return: new_state
    """

    # TODO quando la fase 1 sarà operativa non servirà questo doppio if (Forse)
    if game.Phase == 1:
        if move not in state.moves:
            return state  # Illegal move has no effect
    if game.Phase == 2:
        if move[1] not in state.moves:
            return state  # Illegal move has no effect

    board = state.board.copy()
    new_state = None

    # Check phase
    if state.w_no_board == 0 and state.b_no_board == 0:
        game.Phase = 2

    if game.Phase == 1:
        player = ('B' if state.to_move == 'W' else 'W')
        if MillsGame.check_tris(board, move, state.to_move):
            print("Con questa mossa: " + str(move) + " il " + state.to_move + " ha fatto un TRIS")

        # Scelgo la pedina da eliminare, tenendo in considerazione che le pedine che sono in tris
        # non possono essere eliminate

        # Devo considerare le pedine dell'avversario e per evitare di eliminare pedine che sono in tris
        # uso il metodo check_tris_on_board
        not_removable = MillsGame.check_tris_on_board(game, state, player)

        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        new_state = GameState(to_move=player,
                              utility=compute_utility(game, state),
                              board=board,
                              moves=moves,
                              w_board=(state.w_board + 1 if state.to_move == 'W' else state.w_board),
                              b_board=(state.b_board + 1 if state.to_move == 'B' else state.b_board),
                              w_no_board=(state.w_no_board - 1 if state.to_move == 'W' else state.w_no_board),
                              b_no_board=(state.b_no_board - 1 if state.to_move == 'B' else state.b_no_board)
                              )
    elif game.Phase == 2:
        # move [0] = pedina da muovere
        # move [1] = posizionamento finale
        # print(move)
        player = ('B' if state.to_move == 'W' else 'W')
        if MillsGame.check_tris(board, move[1], state.to_move):
            print("Con questa mossa: " + str(move[1]) + " il " + state.to_move + " ha fatto un TRIS")
         
        board[move[0]] = 'O'
        board[move[1]] = state.to_move
        moves = list(state.moves)
        moves[moves.index(move[1])] = move[0]
        new_state = GameState(to_move=player),
                              utility=compute_utility(game, state),
                              board=board,
                              moves=moves,
                              w_board=state.w_board,
                              b_board=state.b_board,
                              w_no_board=0,
                              b_no_board=0
                              )

    # Prima di fare il return del nuovo stato è necessario calcolare la phase,
    # perchè al termine della result la phase deve essere già a due se con questo mossa entriamo nella seconda phase

    # TODO una volta implementata la result per la fase 2 non serve l'if su new_state not None
    if new_state is not None:
        if new_state.w_no_board == 0 and new_state.b_no_board == 0:
            game.Phase = 2

    return new_state


def compute_utility(game, state):
    """If 'W' wins with this move, return 1; if 'B' wins return -1; else return 0.
    É provvisoria solo per la fase 1
    """
    if game.Phase == 1:
        if state.w_no_board == 0 and state.b_no_board == 0:
            return 1 if state.to_move == 'W' else -1
        else:
            return 0

    else:
        # TODO verificare che can_move se non ci sono mosse mi da una lista vuota
        if state.to_move == 'W' and (state.b_board == 2 or len(MillsGame.can_move(game, state, 'B')) == 0):
            return 1
        elif state.to_move == 'B' and (state.w_board == 2 or len(MillsGame.can_move(game, state, 'W')) == 0):
            return -1
        else:
            return 0
