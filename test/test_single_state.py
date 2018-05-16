from collections import namedtuple

from src.MillsGame import MillsGame
from core.algorithm.aima_alg import *
from src.game_utils import *
GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')

millsGame = MillsGame()

state_phase_one_error_double_game = GameState(to_move='W',
                                              utility=0,
                                              board=['B', 'W', 'O', 'W', 'O', 'O', 'W', 'W', 'W', 'O', 'W', 'O',
                                                     'W', 'O', 'B', 'B', 'B', 'O', 'O', 'W', 'O', 'B', 'O', 'B'],
                                              moves=[2, 4, 5, 13, 18, 20, 22, 9, 11], w_board=8, b_board=5,
                                              w_no_board=1,
                                              b_no_board=1)

state_phase_two = GameState(to_move='W',
                            utility=0,
                            board=['B', 'W', 'O', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'O',
                                   'W', 'O', 'B', 'B', 'B', 'W', 'B', 'W', 'O', 'O', 'O', 'B'],
                            moves=[2, 3, 5, 13, 20, 21, 22, 9, 11], w_board=9, b_board=5, w_no_board=0, b_no_board=0)

# TODO non funziona neanche cosi
state_phase_two_duoble_game = GameState(to_move='W',
                                        utility=0,
                                        board=['B', 'O', 'O', 'W', 'O', 'O', 'W', 'W', 'W', 'W', 'O', 'O',
                                               'W', 'O', 'B', 'B', 'B', 'W', 'W', 'W', 'O', 'B', 'O', 'B'],
                                        moves=[2, 4, 5, 13, 10, 20, 22, 1, 11], w_board=9, b_board=6, w_no_board=0,
                                        b_no_board=0)

# state_phase_two = GameState(to_move='W',
#                             utility=0,
#                             board=['B', 'B', 'O', 'B', 'W', 'B', 'O', 'B', 'O', 'W', 'W', 'O',  # l'ultima è la 11
#                                    'W', 'W', 'W', 'W', 'O', 'O', 'B', 'W', 'O', 'B', 'W', 'O'],
#                             moves=[2, 6, 8, 16, 17, 20, 23, 11], w_board=9, b_board=7, w_no_board=0, b_no_board=0)

millsGame.display(state_phase_two_duoble_game)
moves = millsGame.actions(state_phase_two_duoble_game)
print(state_phase_two_duoble_game)
print("Azioni generate: \n" + str(moves))
new_state = millsGame.result(state_phase_two_duoble_game, moves[0])
print(new_state)
millsGame.display(new_state)


# print(check_couples_phase_two(state_phase_two_duoble_game, 18, 10, 'W'))
