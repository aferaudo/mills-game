
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


def print_current_move(game, old_state, new_state, move, iteration=''):
    print(" --- Iteration " + str(iteration) + " | Player " + old_state.to_move +
          " | " + str(move) + " --- \n")
    game.display(new_state)
    print(new_state, end='\n\n')



def test_phase_one(game, use_random=False):
    print("********* PHASE 1 *********")
    if use_random:
        # player W gioca usando Alpha Beta, B gioca a caso
        current_state = game.initial
        extracted = []
        print(" --- Empty Board --- \n")
        game.display(current_state)
        print(game.initial, end='\n\n')

        iteration = 1
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board,
                          current_state.b_board) == 1:
            end_time = 0.0
            if current_state.to_move == 'W':
                start_time = time.time()
                next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
                end_time = time.time() - start_time
                print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
                extracted.append(next_move[1])
            else:
                start_time = time.time()
                next_move = get_random(extracted)
                end_time = time.time()
                extracted.append(next_move)
                next_move = tuple((-1, next_move, -1))
            old_state = current_state
            # print("Prima di aggiornare lo state")
            # print(old_state)
            current_state = game.result(old_state, next_move)
            # print("Dopo aver aggiornato lo state")
            # print(current_state)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1
            # print("Phase = " + str(game.Phase))

    else:
        # player W gioca usando Alpha Beta, B gioca a caso
        current_state = game.initial
        extracted = []
        print(" --- Empty Board --- \n")
        game.display(current_state)
        print(game.initial, end='\n\n')

        iteration = 1
        while check_phase(current_state.w_no_board, current_state.b_no_board, current_state.w_board, current_state.b_board) == 1:
            end_time = 0.0
            start_time = time.time()
            next_move = alphabeta_cutoff_search(current_state, game, depth, cutt_off, eval_fn)
            end_time = time.time() - start_time
            print("******* TEMPO IMPIEGATO = %s seconds" % end_time)
            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1

    return current_state

# BODY TEST


millsGame = MillsGame()
phase_one_state = test_phase_one(millsGame, True)

print("Le nostre actions per il giocatore " + phase_one_state.to_move)
print(millsGame.actions(phase_one_state))

# move = int(input("Inserisci mossa: "))
# x = int(input("Inserisci tris1: "))
# y = int(input("Inserisci tris1: "))
# z = int(input("Inserisci tris1: "))
# tupla = tuple((x, y, z))
#
# its_adjacents = tupla
# check = 0
# if move in its_adjacents:
#     check = len(its_adjacents)
#     for pos in its_adjacents:
#         if phase_one_state.board[pos] != 'O':
#             check -= 1
# print("Per move: " + str(move) + " check vale: " + str(check))


# print("test funzione calcola pedine bloccate")
# x = int(input("Inserisci mossa: "))
# count_temp = block_pieces(phase_one_state, x)
# print("posizionando la pedina in questa posizione blocco " + str(count_temp) + " pedine avversarie")
# count_temp1 = block_pieces(phase_one_state, x, "B" if phase_one_state.to_move == "W" else "W")
# print("posizionando la pedina in questa posizione blocco " + str(count_temp1) + " pedine mie")

# print("test funzione tris")
# x = int(input("Inserisci tris1: "))
# y = int(input("Inserisci tris1: "))
# z = int(input("Inserisci tris1: "))
# tupla = tuple((x, y, z))
# temp3 = tris_adjacents(tupla)
# print("le adiacenti del tris " + str(tupla) + " sono: " + str(temp3))

# print("********* PHASE 2 *********")
# print("Test game.actions() for player " + phase_one_state.to_move + ": ")
#
# player_actions = millsGame.actions(phase_one_state)
# print(phase_one_state.to_move + ": ")
# print(player_actions)
#
# phase_two_state_1 = millsGame.result(phase_one_state, player_actions[0])
# print_current_move(millsGame, phase_one_state, phase_two_state_1, player_actions[0], 1)
#
# player_actions = millsGame.actions(phase_two_state_1)
# print(phase_two_state_1.to_move + ": ")
# print(player_actions)
# phase_two_state_2 = millsGame.result(phase_two_state_1, player_actions[0])
# print_current_move(millsGame, phase_two_state_1, phase_two_state_2, player_actions[0], 2)


# Stampe prova check_tris
""""player_actions = millsGame.actions(phase_two_state_2)
print(phase_two_state_2.to_move + ": ")
print(player_actions)
x = int(input("Inserisci pedina da muovere "))
y = int(input("Inserisci la mossa "))
tup = (x, y)
phase_two_state_3 = millsGame.result(phase_two_state_2, tup)
print_current_move(millsGame, phase_two_state_2, phase_two_state_3, tup, 3)"""

# Prova can_eliminate

# to_eliminate = can_eliminate(millsGame, phase_two_state_2)
# print("Pedine eliminabili da : " + phase_two_state_2.to_move)
# print(to_eliminate)
# print("Turno di : " + phase_two_state_2.to_move)
# x = int(input("Inserisci pedina da muovere "))
# y = int(input("Inserisci la mossa "))
# tup = (x, y, to_eliminate[0])
# # TODO Problema: Se sposto una pedina che non è quella del turno corrente il programma lo permette.
# phase_two_state_3 = millsGame.result(phase_two_state_2, tup)
# millsGame.display(phase_two_state_3)
# print(can_move(millsGame, phase_one_state, 'B'))

# print(millsGame.player_pieces(phase_one_state))
# print(check_tris_on_board(millsGame, phase_one_state))
# print(check_tris_on_board(millsGame, phase_one_state, "B"))

# print("empty_boxes test: ")
# print(phase_two_state_3.moves)
