from core.Game import Game
from collections import namedtuple
from .gameImplementations.actions import actions
from .gameImplementations.display import display
from .gameImplementations.result import result
from .gameImplementations.terminal_test import terminal_test
from .gameImplementations.utility import utility

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


def locations():
    return [
        [1, 9],  # 0
        [0, 2, 4],  # 1
        [1, 14],  # 2
        [4, 10],  # 3
        [1, 3, 5, 7],  # 4
        [4, 13],  # 5
        [7, 11],  # 6
        [4, 6, 8],  # 7
        [7, 12],  # 8
        [0, 10, 21],  # 9
        [3, 9, 11, 18],  # 10
        [6, 10, 15],  # 11
        [8, 13, 17],  # 12
        [5, 12, 14, 20],  # 13
        [2, 13, 23],  # 14
        [11, 16],  # 15
        [15, 17, 19],  # 16
        [12, 16],  # 17
        [10, 19],  # 18
        [16, 18, 20, 22],  # 19
        [13, 19],  # 20
        [9, 22],  # 21
        [19, 21, 23],  # 22
        [14, 22]  # 23
    ]


def adjacent_locations(position):

    return locations()[position]


def check_tris(state, move):
    tris = [
        [0, 1, 2],
        [0, 9, 21],
        [2, 14, 23],
        [21, 22, 23],
        [3, 4, 5],
        [3, 10, 18],
        [5, 13, 20],
        [18, 19, 20],
        [6, 7, 8],
        [6, 11, 15],
        [8, 12, 17],
        [15, 16, 17],
        [1, 4, 7],
        [9, 10, 11],
        [12, 13, 14],
        [16, 19, 22]
    ]


class MillsGame(Game):

    def __init__(self, size=24, piece=9):
        """
        PHASE
        Proprietà che indica a tutti in che fase del gioco siamo
        """
        # global Phase
        # Phase = 1
        self.Phase = 1
        self.size = size
        self.piece = piece
        moves = [x for x in range(0, self.size)]
        board = ['O' for x in range(0, self.size)]
        self.initial = GameState(to_move='W', utility=0, board=board, moves=moves, w_board=0, b_board=0, w_no_board=self.piece, b_no_board=self.piece)

    def actions(self, state):
        return actions(self, state)

    def result(self, state, move):
        return result(self, state, move)

    def utility(self, state, player):
        return utility(self, state, player)

    def terminal_test(self, state):
        return terminal_test(self, state)

    def display(self, state):
        display(self, state)

    def __str__(self):
        return '<{' + str(self.initial) + '}>'

    def player_pieces(self, state, player=None):
        """
        Restituisce le pedine del giocatore, se :param player non è passato restituisce le pedine del giocatore
        dello stato corrente, altrimenti del giocatore passato tramite il parametro
        :param state:
        :param player:
        :return:
        """
        player = player if player is not None else state.to_move
        pieces = []
        for index, value in enumerate(state.board):
            if value == player:
                pieces.append(index)
        return pieces
