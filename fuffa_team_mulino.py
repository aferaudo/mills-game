import sys, getopt
from src.communication.mysocket import MySocket
from core.algorithm.aima_alg import *
from src.gameImplementations.evaluation import *

GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')

depth = 12
depth_opponent = depth
time_depth = 58
cut_off = None
eval_fn = eval_fn_smart
eval_fn_opponent = eval_fn_opponent


def string_to_state(stringa, our_color):
    info_server = stringa.split("-")

    current_board = []
    for e in info_server[0]:
        current_board.append(e)

    moves = []
    for x, v in enumerate(current_board):
        if v == "O":
            moves.append(x)

    w_board = int(info_server[3].split(",")[0])
    b_board = int(info_server[3].split(",")[1])

    w_no_board = int(info_server[2].split(",")[0])
    b_no_board = int(info_server[2].split(",")[1])

    temp_state = GameState(to_move=('B' if our_color == 'W' else 'W'),
                           utility=0,
                           board=current_board,
                           moves=moves,
                           w_board=w_board,
                           b_board=b_board,
                           w_no_board=w_no_board,
                           b_no_board=b_no_board
                           )
    return GameState(to_move=our_color,
                     utility=compute_utility(temp_state, w_no_board, b_no_board, w_board, b_board),
                     board=current_board,
                     moves=moves,
                     w_board=w_board,
                     b_board=b_board,
                     w_no_board=w_no_board,
                     b_no_board=b_no_board)


def main(argv):
    # prendiamo in ingresso da terminale il colore del giocatore
    our_color = None
    try:
        opts, args = getopt.getopt(argv, "wbh")
    except getopt.GetoptError:
        print('usage: fuffa_team_mulino.py -w (player white) -o (player black)')
        sys.exit(2)
    if len(opts) != 1:
        print('usage: fuffa_team_mulino.py -w (player white) -b (player black)')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: fuffa_team_mulino.py -w (player white) -b (player black)')
            sys.exit()
        elif opt == '-w':
            our_color = 'W'
        elif opt == '-b':
            our_color = 'B'
    if our_color is None:
        print('please specify a player\nusage: fuffa_team_mulino.py -w (player white) -o (player black)')
        sys.exit(2)

    stringa = "OBWOOOOOWWBBOBWOOOOOWWBB-First-6,6-3,3"
    state = string_to_state(stringa, our_color)
    print(str(state))

    # Creazione socket
    python_port = 3033

    python_socket = MySocket()

    # Invio richiesta di connessione alla java interface
    print("Invio la richiesta di connessione alla java interface")
    python_socket.connect('localhost', python_port)
    print("Connessione avvenuta con successo!")

    # Invio il giocatore scelto inserito come parametro
    print("Invio giocatore scelto..")
    python_socket.my_send(our_color.encode("UTF-8"))
    print("Messaggio inviato con successo")

    mills_game = MillsGame()
    current_state = mills_game.initial

    print("Attendo lo stato iniziale")
    state_board = python_socket.receive()
    print(state_board)

    if our_color == 'B':
        # Attendo la mossa bianca
        state_board = python_socket.receive()
        current_state = string_to_state(state_board, our_color)
        print(current_state)

    while not mills_game.terminal_test(current_state):
        next_move = alphabeta_cutoff_search(current_state, mills_game, depth, cut_off, eval_fn, time_depth)
        print("Scrivo la mia mossa: " + str(next_move))
        python_socket.my_send(str(next_move).encode("UTF-8"))
        print("Mossa inviata!")
        print("Attendo il nuovo stato calcolato in base alla mia mossa...")
        state_board = python_socket.receive()
        print("\n\nStato ricevuto: " + state_board)

        print("Attendo la mossa dell'avversario...")
        state_board = python_socket.receive()
        current_state = string_to_state(state_board, our_color)
        print("Mossa ricevuta!")
        print("\n\nNuovo stato dopo la mossa: " + str(current_state))
        # mills_game.display(current_state)
        # print("\n\n")
        # print(current_state)
        # print("\n\n")

    #time.sleep(20)
    #chiusura socket
    python_socket.safely_close()


if __name__ == "__main__":
    main(sys.argv[1:])
