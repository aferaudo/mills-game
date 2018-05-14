
from src.MillsGame import MillsGame
from core.algorithm.aima_alg import alphabeta_cutoff_search
from src.gameImplementations.evaluation import *
import time

depth = 13
eval_fun = None

millsGame = MillsGame()

millsGame.display(millsGame.initial)

start_time = time.time()
move1 = alphabeta_cutoff_search(millsGame.initial, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_1 = millsGame.result(millsGame.initial, move1)
millsGame.display(state_1)

start_time = time.time()
move2 = alphabeta_cutoff_search(state_1, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_2 = millsGame.result(state_1, move2)
millsGame.display(state_2)

start_time = time.time()
move3 = alphabeta_cutoff_search(state_2, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_3 = millsGame.result(state_2, move3)
millsGame.display(state_3)

start_time = time.time()
move4 = alphabeta_cutoff_search(state_3, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_4 = millsGame.result(state_3, move4)
millsGame.display(state_4)

start_time = time.time()
move5 = alphabeta_cutoff_search(state_4, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_5 = millsGame.result(state_4, move5)
millsGame.display(state_5)

start_time = time.time()
move6 = alphabeta_cutoff_search(state_5, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_6 = millsGame.result(state_5, move6)
millsGame.display(state_6)

start_time = time.time()
move7 = alphabeta_cutoff_search(state_6, millsGame, depth, None, eval_fun)
print("Ci ha messo: " + str(time.time()-start_time) + " secondi")
state_7 = millsGame.result(state_6, move7)
millsGame.display(state_7)