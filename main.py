
from src.MillsGame import MillsGame


millsGame = MillsGame(10, 1)

print(millsGame)

newState = millsGame.result(millsGame.initial, 0)

print(newState)

newState2 = millsGame.result(newState, 5)
print(newState2)

print(millsGame.result(newState2, 8))
