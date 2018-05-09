
from src.MillsGame import MillsGame


millsGame = MillsGame(24, 2)
print(" --- Empty Board --- \n")
millsGame.display(millsGame.initial)
print(millsGame.initial, end='\n\n')


move = millsGame.actions(millsGame.initial)[0]
state_1_w = millsGame.result(millsGame.initial, move)
print(" --- Round 1 | Player W | " + str(move) + " --- \n")
millsGame.display(state_1_w)
print(state_1_w, end='\n\n')

move = 5
state_1_b = millsGame.result(state_1_w, move)
print(" --- Round 1 | Player B | " + str(move) + " --- \n")
millsGame.display(state_1_b)
print(state_1_b, end='\n\n')

move = 8
state_2_w = millsGame.result(state_1_b, move)
print(" --- Round 2 | Player W | " + str(move) + " --- \n")
millsGame.display(state_2_w)
print(state_2_w, end='\n\n')

move = 20
state_2_b = millsGame.result(state_2_w, move)
print(" --- Round 2 | Player B | " + str(move) + " --- \n")
millsGame.display(state_2_b)
print(state_2_b, end='\n\n')

print(" --- Testing action for Phase 2 --- ")
print(millsGame.actions(state_2_b))
