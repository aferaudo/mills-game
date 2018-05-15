from core.Game import Game
from collections import namedtuple
from .gameImplementations.display import display
from .gameImplementations.result import result
from .gameImplementations.terminal_test import terminal_test
from .gameImplementations.utility import utility
from .gameImplementations.filter_actions import *

"""
Game State
to_move = rappresenta di chi è il turno corrente
utility = 1 con la prossima mossa vinciamo, -1 perdiamo, 0 non succede
board = rappresentazione della board
moves = possibili mosse a partire dallo stato corrente
w_board = pedine bianche sulla board
b_board = pedine nere sulla board
w_no_board = pedine bianche ancora da mettere in gioco
b_no_board = pedine n ere ancora da mettere in gioco
"""
GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')


class MillsGame(Game):

    def __init__(self, size=24, piece=9):
        """
        PHASE
        Proprietà che indica a tutti in che fase del gioco siamo
        """
        # global Phase
        # Phase = 1
        self.Phase = 1
        self.TempPhase = 1
        self.size = size
        self.piece = piece
        moves = [x for x in range(0, self.size)]
        board = ['O' for x in range(0, self.size)]
        self.initial = GameState(to_move='W', utility=0, board=board, moves=moves, w_board=0, b_board=0, w_no_board=self.piece, b_no_board=self.piece)

    def actions(self, state):
        """
            prende in ingresso lo stato corrente (disposizione pedine sulla board) e restituisce
            le azioni fattibili dal giocatore che sta muovendo in base alla fase di gioco corrente
            fase 1: disposizione iniziale delle pedine sulla board
            fase 2: movimento pedine sulla board da una posizione ad una adiacente
            fase 3: movimento pedine sulla board da una posizione ad un'altra qualsiasi
            :param self:
            :param state:
            :return:
            """
        moves = state.moves
        player = state.to_move

        phase = check_phase(state.w_no_board, state.b_no_board, state.w_board, state.b_board)

        # print("Phase in actions: " + str(self.Phase))

        if phase == 1:
            moves = filter_phase1(self, state)

        if phase == 2:
            moves = filter_phase2(self, state)

        if phase == 3:
            moves = filter_phase3(self, state)
        return moves

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

