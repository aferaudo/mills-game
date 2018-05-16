
def locations():
    """
    restituisce una lista contenente tutte le posizioni adiacenti alle diverse posizioni possibili sulla board
    :return:
    """
    return [
        [1, 9],  # 0
        [0, 2, 4],  # 1
        [1, 14],  # 2
        [4, 10],  # 3
        [1, 3, 5, 7],  # 4
        [4, 13],  # 5
        [7, 11],  # 6
        [4, 6, 8],  # 7
        [7, 12],  # 8
        [0, 10, 21],  # 9
        [3, 9, 11, 18],  # 10
        [6, 10, 15],  # 11
        [8, 13, 17],  # 12
        [5, 12, 14, 20],  # 13
        [2, 13, 23],  # 14
        [11, 16],  # 15
        [15, 17, 19],  # 16
        [12, 16],  # 17
        [10, 19],  # 18
        [16, 18, 20, 22],  # 19
        [13, 19],  # 20
        [9, 22],  # 21
        [19, 21, 23],  # 22
        [14, 22]  # 23
    ]


def all_tris():
    """
    restituisce una lista contenente tutti i possibili tris che si possono formare sulla board
    :return:
    """
    return [
        [0, 1, 2],
        [0, 9, 21],
        [2, 14, 23],
        [21, 22, 23],
        [3, 4, 5],
        [3, 10, 18],
        [5, 13, 20],
        [18, 19, 20],
        [6, 7, 8],
        [6, 11, 15],
        [8, 12, 17],
        [15, 16, 17],
        [1, 4, 7],
        [9, 10, 11],
        [12, 13, 14],
        [16, 19, 22]
    ]


def player_pieces(state, player=None):
    """
    Restituisce le pedine del giocatore, se :param player non è passato restituisce le pedine del giocatore
    dello stato corrente, altrimenti del giocatore passato tramite il parametro
    :param state:
    :param player:
    :return:
    """
    player = player if player is not None else state.to_move
    pieces = []
    for index, value in enumerate(state.board):
        if value == player:
            pieces.append(index)
    return pieces


def adjacent_locations(position):
    """
    prende in ingresso una posizione e restituisce le sue adiacenti
    :param position:
    :return:
    """
    return locations()[position]


def check_tris_on_board(state, player=None, count_check=3):
    """
    Restituisce la lista dei tris fatti sulla board fatti dal giocatore corrente se player non è passato, altrimenti
    calcola i tris del giocatore passato
    :param game:
    :param state:
    :param player:
    :param count_check:
    :return tris_done:
    """
    p_pieces = player_pieces(state, player)
    tris_done = []
    for tris in all_tris():
        count = 0
        for pos in tris:
            if pos in p_pieces:
                count += 1
        if count == count_check:
            tris_done.append(tris)

    return tris_done


# TODO Non siamo sicuri che questo sia un metodo realmente utile
def will_tris(game, state, player=None):
    """
    restituisce una lista contenente le mosse che se fatte portano ad un tris
    :param game:
    :param state:
    :param player:
    :return:
    """
    tris = []
    if game.Phase == 1:
        tris.extend(check_tris_on_board(game, state, player, 2))
        # TODO Controllare che il terzo vicino sia vuoto
    else:
        print()
        # TODO Prima facciamo la result della Phase 2
        # Vogliamo simulare l'aggiornamento di stato usando game.result e poi controlliamo se nel nuovo stato si
        # verifica un tris, ma prima devo salvare i tris che ho già

    return tris


def check_tris(board, old_pos, pos_fin, player):
    """
    Controlla se con la mossa da effettuare si realizza un tris
    :param board:
    :param old_pos:
    :param pos_fin:
    :param player:
    :return: boolean
    """
    for tris in all_tris():
        if pos_fin in tris:
            count = 0
            for pos in tris:
                if pos != pos_fin and board[pos] == player and old_pos != pos:
                    count += 1
                if count == 2:
                    return True

    return False


def can_eliminate(state):
    """
    prende in ingresso lo stato il giocatore che deve muovere
    restituisce tutte le pedine dell'aversario che si possono eliminare
    :param game:
    :param state:
    :param player:
    :return:
    """
    player = 'B' if state.to_move == 'W' else 'W'
    opponent_pieces = player_pieces(state, player)
    tris_done = check_tris_on_board(state, player)
    not_removable = []
    for tris in tris_done:
        for x in tris:
            not_removable.append(x)

    removable = list(set(opponent_pieces) - set(not_removable))

    return removable


def can_move(state, player=None):
    """
    restituisce una lista di tuple come (posizione corrente, mossa possibile, pedine dell'avversario che posso eliminare)
    :param game:
    :param state:
    :param player:
    :return:
    """
    player = player if player is not None else state.to_move

    moves = []
    removable = can_eliminate(state)
    for index, value in enumerate(state.board):
        if value == player:
            for pos in adjacent_locations(index):
                if state.board[pos] == 'O':
                    if check_tris(state.board, index, pos, player):
                        for r in removable:
                            moves.append(tuple((index, pos, r)))
                    else:
                        moves.append(tuple((index, pos, -1)))

    return moves


def remove_moves_occupied(state, moves):
    """
    Prende una lista di mosse e rimuove le posizioni già occupate guardando la board (state.board)
    :param state:
    :param moves:
    :return:
    """
    for index, value in enumerate(state.board):
        if value != 'O':
            if index in moves:
                moves.remove(index)

    return moves


def check_double_game(state, move, player=None):
    """
    questa funzione prende in ingresso lo stato e una possibile mossa
    restituisce vero se con questa mossa si forma un doppio gioco
    :param state:
    :param move:
    :param player:
    :return:
    """
    player = player if player is not None else state.to_move

    if check_couples(state, move, player) == 2:
        return True
    else:
        return False


def check_couples(state, move, player=None):
    """
    questa funzione prende in ingresso lo stato e una possibile mossa
    restituisce il numero di coppie che si formerebbero
    :param state:
    :param move:
    :param player:
    :return:
    """
    player = player if player is not None else state.to_move

    tris_presence = 0
    for tris in all_tris():
        if move in tris:
            two_empty = 0
            one_my_color = 0
            for pos in tris:
                if pos != move and state.board[pos] == player:
                    one_my_color += 1
                if state.board[pos] == 'O':
                    two_empty += 1
            if one_my_color == 1 and two_empty == 2:
                tris_presence += 1

    return tris_presence


def block_pieces(state, move, player=None):
    """
    questa funzione prende in ingresso una posizione e un giocatore se specificato
    ritorna il numero di pedine avversarie che con questa mossa non possono più muoversi
    :param state:
    :param player:
    :return:
    """

    player = player if player is not None else state.to_move
    opponent = "B" if player == "W" else "W"

    blocked_pieces = 0

    # print("devo valutare il posizionamento in posizione " + str(move))
    # print("sta giocando il giocatore " + player)
    # print("le adiacenti della mossa sono: " + str(locations()[move]))
    for adjacent in locations()[move]:
        if state.board[adjacent] == opponent:
            # print("pedina avversaria adiacente da controllare: " + str(adjacent))
            opponent_adjacentsss = locations()[adjacent]
            # print("le sue adiacenti sono: " + str(opponent_adjacentsss))
            check = len(opponent_adjacentsss)-1
            # print("check prima dei controlli vale: " + str(check))
            for opponent_adjacent in opponent_adjacentsss:
                if opponent_adjacent != move and state.board[opponent_adjacent] != 'O':
                    check -= 1
            # print("check alla fine dei controlli vale: " + str(check))
            if check == 0:
                blocked_pieces += 1

    return blocked_pieces


def tris_adjacents(tris):
    """
    questa funzione prende in ingresso un tris e restituisce una lista contenente tutte le adiacenti
    di quel tris
    :param tris:
    :return:
    """
    adjacents = []

    # inserisco tutte le adiacenti di ogni elemento del tris
    for x in tris:
        for y in locations()[x]:
            adjacents.append(y)

    # elimino dalle adiacenti quelle che fanno parte del tris
    for x in tris:
        adjacents = list(filter(lambda a: a != x, adjacents))

    return adjacents


def check_phase(w_no_board, b_no_board, w_board, b_board):
    """
    Controllo in base allo stato in quale fase siamo e restituisce il numero della fase
    :param state:
    :return:
    """
    if w_no_board == 0 and b_no_board == 0:
        return 2
    else:
        return 1
    # TODO check per la fase 3


def all_pieces_on_board(state):
    """
    Metodo che restituisce tutte le pedine presenti nella board, senza distinzioni tra i giocatori
    :param state:
    :return:
    """
    # TODO valutare se separare le pedine per giocatore restituendo un dictionary {W: pieces, B: pieces}
    pieces = []
    for index, value in enumerate(state.board):
        if value != 'O':
            pieces.append(index)

    return pieces


def all_tris_on_board(state, count_check=3):
    """
    Restituisce un dictionary con tutti i tris fatti da W e tutti i tris fatti da B
    :param game:
    :param state:
    :param player:
    :param count_check:
    :return tris_done:
    """
    all_pieces = all_pieces_on_board(state)
    tris_done_w = []
    tris_done_b = []

    for tris in all_tris():
        count_w = 0
        count_b = 0
        for pos in tris:
            if pos in all_pieces and state.board[pos] == 'W':
                count_w += 1
            if pos in all_pieces and state.board[pos] == 'B':
                count_b += 1
        if count_w == count_check:
            tris_done_w.append(tris)
        if count_b == count_check:
            tris_done_b.append(tris)

    return {
        'W': tris_done_w,
        'B': tris_done_b
    }


