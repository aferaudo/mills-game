from collections import namedtuple

from src.MillsGame import MillsGame
from core.algorithm.aima_alg import *
from src.game_utils import *
from src.gameImplementations.evaluation import *
from src.Logger import Logger

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

state_phase_two_tris_trick = GameState(to_move='W',
                                       utility=0,
                                       board=['B', 'O', 'W', 'W', 'O', 'W', 'W', 'O', 'O', 'O', 'O', 'O',
                                              'O', 'W', 'B', 'B', 'B', 'O', 'W', 'W', 'W', 'B', 'W', 'B'],
                                       moves=[9, 4, 8, 12, 10, 17, 7, 1, 11], w_board=9, b_board=6, w_no_board=0,
                                       b_no_board=0)

# state_phase_two = GameState(to_move='W',
#                             utility=0,
#                             board=['B', 'B', 'O', 'B', 'W', 'B', 'O', 'B', 'O', 'W', 'W', 'O',  # l'ultima è la 11
#                                    'W', 'W', 'W', 'W', 'O', 'O', 'B', 'W', 'O', 'B', 'W', 'O'],
#                             moves=[2, 6, 8, 16, 17, 20, 23, 11], w_board=9, b_board=7, w_no_board=0, b_no_board=0)

state_phase_two_end = GameState(to_move='B',
                                utility=0,
                                board=['O', 'W', 'O', 'B', 'W', 'B', 'O', 'B', 'O', 'O', 'B', 'O',
                                       'W', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'B', 'B', 'O', 'B'],
                                moves=[0, 2, 8, 17, 9, 14, 6, 11, 22], w_board=8, b_board=7, w_no_board=0, b_no_board=0)

state_phase_three_start = GameState(to_move='B',
                                    utility=0,
                                    board=['O', 'W', 'O', 'B', 'W', 'B', 'O', 'O', 'O', 'O', 'O', 'O',
                                           'O', 'O', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'O', 'B'],
                                    moves=[0, 2, 8, 12, 10, 14, 6, 11, 22, 9, 21, 13, 7], w_board=8,
                                    b_board=3, w_no_board=0, b_no_board=0)

state_phase_three_test = GameState(to_move='B',
                                   utility=0,
                                   board=['O', 'W', 'O', 'W', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'W',
                                          'O', 'O', 'B', 'B', 'W', 'W', 'O', 'O', 'W', 'O', 'O', 'B'],
                                   moves=[0, 4, 8, 12, 18, 5, 6, 2, 22, 9, 21, 13, 7, 19], w_board=7, b_board=3,
                                   w_no_board=0, b_no_board=0)

state_delete_for_win = GameState(to_move='W',
                                 utility=0,
                                 board=['B', 'B', 'W', 'W', 'W', 'O', 'B', 'W', 'B', 'B', 'B', 'W',
                                        'O', 'W', 'O', 'O', 'O', 'O', 'B', 'W', 'O', 'W', 'B', 'W'],
                                 moves=[12, 14, 15, 16, 17, 20, 5], w_board=9, b_board=8, w_no_board=0, b_no_board=0)

state_run_error = GameState(to_move='W',
                            utility=0,
                            board=['W', 'O', 'W', 'B', 'W', 'W', 'B', 'B', 'O', 'B', 'W', 'B',
                                   'B', 'W', 'B', 'W', 'B', 'W', 'O', 'O', 'B', 'O', 'O', 'O'],
                            moves=[18, 1, 8, 19, 21, 22, 23], w_board=8, b_board=9, w_no_board=0, b_no_board=0)

state_run_error_due = GameState(to_move='W', utility=0, board=['O', 'W', 'O', 'B', 'W', 'B', 'O', 'B', 'O', 'B', 'B', 'W', 'W', 'W', 'B', 'W', 'W', 'O', 'W', 'W', 'B', 'O', 'B', 'B'], moves=[0, 2, 6, 8, 17, 21], w_board=9, b_board=9, w_no_board=0, b_no_board=0)

temp_state = GameState(to_move='B',
                       utility=0,
                       board=['W', 'W', 'B', 'O', 'B', 'B', 'B', 'B', 'W', 'O', 'B', 'W',
                              'O', 'W', 'O', 'O', 'W', 'W', 'W', 'W', 'B', 'B', 'O', 'B'],
                       moves=[3, 14, 12, 15, 9, 22], w_board=9, b_board=9, w_no_board=0, b_no_board=0)

temp_two_state = GameState(to_move='W',
                           utility=0,
                           board=['B', 'B', 'W', 'O', 'W', 'W', 'W', 'W', 'B', 'O', 'W', 'B',
                                  'O', 'B', 'O', 'O', 'B', 'B', 'B', 'B', 'W', 'W', 'O', 'W'],
                           moves=[3, 14, 12, 15, 9, 22], w_board=9, b_board=9, w_no_board=0, b_no_board=0)
# TODO testare loop partita
look_delete = GameState(to_move='B',
                        utility=0,
                        board=['O', 'B', 'O', 'W', 'W', 'W', 'B', 'W', 'B', 'O', 'B', 'O',
                               'B', 'W', 'W', 'O', 'W', 'B', 'O', 'B', 'B', 'O', 'W', 'O'],
                        moves=[0, 11, 15, 18, 9, 23, 2, 21], w_board=8, b_board=8, w_no_board=0, b_no_board=0)

loop_to_delete = GameState(to_move='B',
                           utility=0,
                           board=['O', 'B', 'O', 'W', 'W', 'W', 'B', 'B', 'O', 'O', 'B', 'O',
                                  'B', 'W', 'W', 'O', 'O', 'W', 'O', 'B', 'B', 'O', 'O', 'O'],
                           moves=[0, 11, 15, 18, 9, 22, 23, 21, 8, 16, 2], w_board=6, b_board=7, w_no_board=0, b_no_board=0)
# TODO fare partita giocando da nero

# millsGame.display(state_phase_three_start)
# print("State = " + str(state_phase_three_start))
# moves = millsGame.actions(state_phase_three_start)
# print("Moves = " + str(moves))

# logger = Logger()

# logger.save_state(look_delete, 'look_delete.txt')

millsGame.display(state_run_error_due)
print("State = " + str(state_run_error_due))
moves = millsGame.actions(state_run_error_due)
print("Moves = " + str(moves))

depth = 3

next_move = alphabeta_cutoff_search(state_run_error_due, millsGame, depth, None, eval_fn_smart)
print(next_move)

next_state = millsGame.result(state_run_error_due, next_move)
millsGame.display(next_state)
print(next_state)

next_move = alphabeta_cutoff_search(next_state, millsGame, depth, None, eval_fn_smart)
print(next_move)

next_state = millsGame.result(next_state, next_move)
millsGame.display(next_state)
print(next_state)

# print("State = " + str(state_phase_three_test))
# moves = millsGame.actions(state_phase_three_test)
# print("Moves = " + str(moves))
#
# depth = 8
# move = alphabeta_cutoff_search(state_phase_three_test, millsGame, depth, None, eval_fn_stupid)
# print("AlfaBeta move = " + str(move))
#
# next_state = millsGame.result(state_phase_three_test, move)
# millsGame.display(next_state)
# print("stato = " + str(next_state))


# print(check_couples_phase_two(state_phase_two_duoble_game, 18, 10, 'W'))
