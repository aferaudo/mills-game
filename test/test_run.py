from src.MillsGame import MillsGame, can_eliminate
from core.algorithm.aima_alg import *
from src.game_utils import *
from src.gameImplementations.delete_strategy import delete_pieces_phase1

import time
import random

depth = 5
cutt_off = None
eval_fn = None


def get_random(extracted):
    """
    Restituisce un numero random evitando le collisioni
    :param extracted:
    :return random:
    """
    index_not_found = True
    index = None
    while index_not_found:
        index = random.randint(0, 23)
        if index not in extracted:
            index_not_found = False

    return index


def get_random_action(actions):
    """
    Restituisce un numero random evitando le collisioni
    :param extracted:
    :return random:
    """
    return random.randint(0, len(actions))


def print_current_move(game, old_state, new_state, move, iteration=''):
    print(" --- Iteration " + str(iteration) + " | Player " + old_state.to_move +
          " | " + str(move) + " --- \n")
    game.display(new_state)
    print(new_state, end='\n\n')


def test_phase_one(game, mode=1):
    """
    Testa la fase 1 in modalità differenti in base al valore di mode:
        - mode = 1 -> AI vs Random
        - mode = 2 -> AI vs AI
        - mode = 3 -> AI vs Human
        - mode = 4 -> Human vs AI
    :param game:
    :param mode:
    :return:
    """
    print("********* PHASE 1 *********\n")
    current_state = game.initial
    extracted = []
    print(" --- Empty Board --- \n")
    game.display(current_state)
    print(game.initial, end='\n\n')

    iteration = 1
    if mode == 1:
        # player W gioca usando Alpha Beta, B gioca a caso

        print("--- AI vs Random ---\n\n")
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board) == 1:
            if current_state.to_move == 'W':
                start_time = time.time()
                next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
                extracted.append(next_move[1])
            else:
                start_time = time.time()
                next_move = get_random(extracted)
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
                extracted.append(next_move)
                next_move = tuple((-1, next_move, -1))
            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1

    elif mode == 2:
        # player W e B giocano usando Alpha Beta

        print("--- AI vs AI ---\n\n")
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board) == 1:
            start_time = time.time()
            next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
            end_time = time.time() - start_time
            print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1

    elif mode == 3:
        # player W gioca usando Alpha Beta, B è politato dall'utente

        print("--- AI vs Human ---\n\n")
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board) == 1:
            if current_state.to_move == 'W':
                start_time = time.time()
                next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
                extracted.append(next_move[1])
            else:
                next_move = int(input("Inserisci la tua mossa tra queste " + str(current_state.moves) + "\n"))
                if check_tris(current_state.board, -1, next_move, 'B'):
                    delete_pos = int(input("Quale pedina avversaria vuoi eliminare tra queste: \n" + str(can_eliminate(current_state))))
                else:
                    delete_pos = -1
                next_move = tuple((-1, next_move, delete_pos))
            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1
    elif mode == 4:
        # player B gioca usando Alpha Beta, W è politato dall'utente

        print("--- Human vs AI ---\n\n")
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board) == 1:
            if current_state.to_move == 'B':
                start_time = time.time()
                next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
                extracted.append(next_move[1])
            else:
                next_move = int(input("Inserisci la tua mossa tra queste " + str(current_state.moves) + "\n"))
                if check_tris(current_state.board, -1, next_move, 'B'):
                    delete_pos = int(input("Quale pedina avversaria vuoi eliminare tra queste: \n" + str(can_eliminate(current_state))))
                else:
                    delete_pos = -1
                next_move = tuple((-1, next_move, delete_pos))
            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1

    return current_state


def test_phase_two(game, state, mode=1):
    print("********* PHASE 2 *********\n")

    if mode == 1:

        current_state = state
        iteration = 1
        extracted = []
        print(check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board))
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board) == 2:
            if current_state.to_move == 'W':
                start_time = time.time()
                next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
            else:
                start_time = time.time()
                actions = game.actions(current_state)
                next_move_index = get_random_action(actions)
                next_move = actions[next_move_index]
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)

            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1
            print("fase")
            print(check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                              current_state.b_board))

    return current_state


# BODY TEST


millsGame = MillsGame()
# mode = 2
mode = input("Scegli in quale modalità giocare: \n"
             "- mode = 1 -> AI vs Random \n"
             "- mode = 2 -> AI vs AI \n"
             "- mode = 3 -> AI vs Human \n"
             "- mode = 4 -> Human vs AI\n")
phase_one_state = test_phase_one(millsGame, int(mode))

# print("Le nostre actions per il giocatore " + phase_one_state.to_move)
# print(millsGame.actions(phase_one_state))
phase_two_state = test_phase_two(millsGame, phase_one_state, int(mode))
print(phase_two_state)
