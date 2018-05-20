
from ..utilis.aima_utils import argmax
import time

infinity = float('inf')

# ______________________________________________________________________________
# Minimax Search


def minimax_decision(state, game):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states. [Figure 5.3]"""

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        return v

    # Body of minimax_decision:
    return argmax(game.actions(state),
                  key=lambda a: min_value(game.result(state, a)))

# ______________________________________________________________________________
# Alpha Beta Search


def alphabeta_search(state, game):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = game.to_move(state)

    # Functions used by alphabeta
    def max_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_cutoff_search:
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

# ______________________________________________________________________________
# Alpha Beta Cutoff Search


def alphabeta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None, time_depth=50, logger=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    # TODO togliere i log

    player = game.to_move(state)

    start_time = time.time()

    if logger is not None:
        logger.init_log_file('alpha_beta')

    def cut_off_timer(state, depth):
        """
        La nostra cutoff_test che ferma l'algoritmo dopo che sono trascorsi time_depth secondi
        :param state:
        :param depth:
        :return:
        """
        end_time = time.time() - start_time
        if depth > d or game.terminal_test(state) or end_time > time_depth:
            return True

    # Functions used by alphabeta
    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            eval_value = eval_fn(state, player)
            to_print = "Eval value = " + str(eval_value) + "\nStato della eval = " + str(state) \
                       + "\n----------------------\n\n"
            if logger is not None:
                logger.info_message(to_print)
            return eval_value
        v = -infinity
        for a in game.actions(state):
            to_print = "Giocatore = " + state.to_move + "\nProfondità esplorata = " + str(depth) \
                       + "\nMossa corrente = " + str(a) + "\nState = " + str(state) + "\n----------------------\n\n"
            if logger is not None:
                logger.info_message(to_print)

            # print("Giocatore = " + state.to_move)
            # print("Profondità esplorata = " + str(depth))
            # print("Mossa corrente = " + str(a))
            # print("State = " + str(state))
            # print("----------------------\n\n")
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            eval_value = eval_fn(state, player)

            to_print = "Eval value = " + str(eval_value) + "\nStato della eval = " + str(state) \
                       + "\n----------------------\n\n"
            if logger is not None:
                logger.info_message(to_print)
            # print("Eval value = " + str(eval_value))
            # print("----------------------\n\n")

            return eval_value
        v = infinity
        for a in game.actions(state):
            to_print = "Giocatore = " + state.to_move + "\nProfondità esplorata = " + str(depth) \
                       + "\nMossa corrente = " + str(a) + "\nState = " + str(state) + "\n----------------------\n\n"
            if logger is not None:
                logger.info_message(to_print)
            # print("Giocatore = " + state.to_move)
            # print("Profondità esplorata = " + str(depth))
            # print("Mossa corrente = " + str(a))
            # print("State = " + str(state))
            # print("----------------------\n\n")
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_cutoff_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or cut_off_timer)
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        to_print = "Giocatore = " + state.to_move + "\nProfondità esplorata = " + str(0) \
                   + "\nMossa corrente = " + str(a) + "\nState = " + str(state) + "\n----------------------\n\n"
        if logger is not None:
            logger.info_message(to_print)

        # print("Giocatore = " + state.to_move)
        # print("Profondità esplorata = " + str(0))
        # print("Mossa corrente = " + str(a))
        # print("State = " + str(state))
        # print("----------------------\n\n")
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a

    if logger is not None:
        logger.info_message("******* BEST ACTION = " + str(best_action) + " *******\n\n")
    return best_action
