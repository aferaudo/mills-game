
from src.MillsGame import MillsGame

millsGame = MillsGame()

print(millsGame)

newState = millsGame.result(millsGame.initial, 0)

print(newState)
print(millsGame.result(newState, 5))