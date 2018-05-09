
from src.MillsGame import MillsGame


millsGame = MillsGame(24, 1)
millsGame.display(millsGame.initial)
print(millsGame)

move = millsGame.actions(millsGame.initial)[0]

newState = millsGame.result(millsGame.initial, move)
millsGame.display(newState)
print(newState)

newState2 = millsGame.result(newState, 5)
print(newState2)
millsGame.display(newState2)
print(millsGame.result(newState2, 8))
