
from src.MillsGame import MillsGame, can_move
import random


def get_random(extracted):
    """
    Restituisce un numero random evitando le collisioni
    :param extracted:
    :return random:
    """
    index_not_found = True
    index = None
    while index_not_found:
        index = random.randint(0, 24)
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
        current_state = game.initial
        extracted = []
        print(" --- Empty Board --- \n")
        game.display(current_state)
        print(game.initial, end='\n\n')

        first_move = game.actions(current_state)[0]
        extracted.append(first_move)
        current_state = game.result(current_state, first_move)

        print_current_move(game, game.initial, current_state, first_move, 1)

        iteration = 2
        while game.Phase == 1:
            next_move = get_random(extracted)
            extracted.append(next_move)
            old_state = current_state
            current_state = game.result(old_state, next_move)
            print_current_move(game, old_state, current_state, next_move, iteration)
            iteration += 1

        return current_state

# BODY TEST


millsGame = MillsGame()
phase_one_state = test_phase_one(millsGame, True)

print("********* PHASE 2 *********")
print("Test game.actions() for player " + phase_one_state.to_move + ": ")

player_actions = millsGame.actions(phase_one_state)
print(phase_one_state.to_move + ": ")
print(player_actions)

phase_two_state_1 = millsGame.result(phase_one_state, player_actions[0])
print_current_move(millsGame, phase_one_state, phase_two_state_1, player_actions[0], 1)

player_actions = millsGame.actions(phase_two_state_1)
print(phase_two_state_1.to_move + ": ")
print(player_actions)
phase_two_state_2 = millsGame.result(phase_two_state_1, player_actions[0])
print_current_move(millsGame, phase_two_state_1, phase_two_state_2, player_actions[0], 2)

# print(can_move(millsGame, phase_one_state, 'B'))

# print(millsGame.player_pieces(phase_one_state))
# print(check_tris_on_board(millsGame, phase_one_state))
# print(check_tris_on_board(millsGame, phase_one_state, "B"))
