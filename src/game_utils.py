

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
    opponent = 'B' if state.to_move == 'W' else 'W'
    opponent_pieces = player_pieces(state, opponent)

    if (opponent == "B" and state.b_board == 3) or (opponent == "W" and state.w_board == 3):
        # se l'avversario è in fase 3 non devo controllare se ha dei tris, perchè posso eliminare quello che voglio
        return opponent_pieces

    tris_done = check_tris_on_board(state, opponent)
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
    for index, value in enumerate(state.board):
        if value == player:
            for pos in adjacent_locations(index):
                if state.board[pos] == 'O':
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


def check_couples(state, move, player=None, is_delete=False):
    """
    questa funzione prende in ingresso lo stato e una possibile mossa
    restituisce il numero di coppie che si formerebbero
    :param state:
    :param move:
    :param player:
    :param is_delete:
    :return:
    """
    player = player if player is not None else state.to_move

    num_my_color = 1
    num_empty = 2
    if is_delete:
        num_my_color = 2
        num_empty = 1

    couple_presences = 0
    for tris in all_tris():
        if move in tris:
            two_empty = 0
            one_my_color = 0
            for pos in tris:
                if pos != move and state.board[pos] == player and not is_delete:
                    one_my_color += 1
                if state.board[pos] == player and is_delete:
                    one_my_color += 1
                if state.board[pos] == 'O':
                    two_empty += 1
            if one_my_color == num_my_color and two_empty == num_empty:
                couple_presences += 1

    return couple_presences


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


def check_phase(w_no_board, b_no_board, w_board, b_board, player):
    """
    Controllo in base allo stato in quale fase siamo e restituisce il numero della fase
    :param w_no_board:
    :param b_no_board:
    :param w_board:
    :param b_board:
    :param player:
    :return:
    """

    if w_no_board == 0 and b_no_board == 0 and w_board == 3 and player == "W":
        return 3
    elif w_no_board == 0 and b_no_board == 0 and b_board == 3 and player == "B":
        return 3
    elif w_no_board == 0 and b_no_board == 0:
        return 2
    else:
        return 1


def all_pieces_on_board(state):
    """
    Metodo che restituisce tutte le pedine presenti nella board, senza distinzioni tra i giocatori
    :param state:
    :return:
    """
    # valutare se separare le pedine per giocatore restituendo un dictionary {W: pieces, B: pieces}
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


def unlock_opponent_tris_trick(opponent_tris, old_pos):
    """
    Questo metodo controlla se la posizione di partenza della fase 2 sblocca un tris eventualmente bloccato in precedenza
    :param opponent_tris:
    :param old_pos:
    :param new_pos:
    :param opponent:
    :return:
    """

    if len(opponent_tris) > 0:
        # itero tutti i tris e cerco gli adiacenti del tris
        for tris in opponent_tris:
            adjacent_of_this_tris = tris_adjacents(tris)
            if old_pos in adjacent_of_this_tris:
                return True
        return False
    else:
        return False


def check_couples_phase_two(state, old_pos, move, player=None):
    """
    questa funzione prende in ingresso lo stato e una possibile mossa
    restituisce il numero di coppie che si formerebbero nella fase due considerando anche la posizione di partenza
    :param state:
    :param old_pos:
    :param move:
    :param player:
    :return:
    """
    player = player if player is not None else state.to_move

    couple_presence = 0
    for tris in all_tris():
        if move in tris:
            two_empty = 0
            one_my_color = 0
            for pos in tris:
                if pos != move and pos != old_pos and state.board[pos] == player:
                    one_my_color += 1
                if state.board[pos] == 'O':
                    two_empty += 1
            if one_my_color == 1 and two_empty == 2:
                couple_presence += 1

    return couple_presence


def move_in_player_tris(board, player_tris, move, opponent):
    """
    Controlla se la mossa passata appartiene ad uno dei tris già fatti dal giocatore passato
    se appartiene ad un tris, restituisce il tris, altrimenti False. Restituisce False anche se gli adiacenti della mossa
    corrente sono occupati da pedine dell'avversario
    N.B. restituisco subito il primo tris, perchè se la pedina è in due tris, vuol dire che non si può muovere e quindi
    non ha senso questo controllo
    :param board
    :param player_tris:
    :param move:
    :param opponent
    :return:
    """

    # non controlla se l'avversario sta per fare tris, deve controllarlo l'algoritmo quando si esegue
    for tris in player_tris:
        if move in tris:
            adjacent = adjacent_locations(move)
            for pos in adjacent:
                if board[pos] == opponent:
                    return False
            return True

    return False


def move_block_tris_phase_3(state, move, opponent):
    """
    Controlla se l'avversario ha una coppia con cui può fare tris al turno successivo
    :param state:
    :param move:
    :param opponent:
    :return:
    """

    possible_tris = check_tris_with_return(state.board, -1, move, opponent)

    if possible_tris is not None:
        possible_tris.remove(move)
        move_adjacent = list(set(adjacent_locations(move))-set(possible_tris))
        for pos in move_adjacent:
            if state.board[pos] == opponent:
                return True

    return False


def check_tris_with_return(board, old_pos, pos_fin, player):
    """
    Controlla se con la mossa da effettuare si realizza un tris e nel caso lo restituisce
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
                    return tris

    return None


def check_couples_future_tris_delete(state, move, player=None):
    """
    questa funzione prende in ingresso lo stato e una possibile mossa
    restituisce il numero di coppie che si formerebbero
    :param state:
    :param move:
    :param player:
    :param is_delete:
    :return:
    """
    player = player if player is not None else state.to_move

    empty_positions = []
    for tris in all_tris():
        if move in tris:
            one_empty = 0
            two_my_color = 0
            for pos in tris:
                if state.board[pos] == player:
                    two_my_color += 1
                if state.board[pos] == 'O':
                    one_empty += 1
                    # mi salvo la posizione della casella vuota per poi restituirla se c'è una coppia
                    empty_pos = pos
            if two_my_color == 2 and one_empty == 1:
                empty_positions.append(empty_pos)

    return empty_positions


def check_future_tris(cuple_empty_position, board, player):
    """
    Prende in ingresso la lista delle posizioni vuote delle coppie di un giocatore e controlla quante di queste posizioni
    hanno un adiacente dello stesso giocatore e che quindi lo porterebbe a fare un tris
    :param cuple_empty_position:
    :param board:
    :param player:
    :return:
    """

    future_tris_count = 0
    for empty_pos in cuple_empty_position:
        adjacent = adjacent_locations(empty_pos)
        count_of_player_pieces = 0
        for pos in adjacent:
            if board[pos] == player:
                count_of_player_pieces += 1
        if count_of_player_pieces >= 2:
            future_tris_count += 1

    return future_tris_count


def will_tris(board, piece, player):
    """
    Controlla se gli adiacenti di una pedina possono fare tris muovendosi
    :param board:
    :param piece:
    :param player:
    :return:
    """

    move_adjacent = adjacent_locations(piece)
    for pos in move_adjacent:
        if check_tris(board, piece, pos, player):
            return True


def all_pieces_on_board_for_each_player(state):
    """
    Metodo che restituisce tutte le pedine presenti nella board, inserendo in un dictionary le pedine di due giocatori
    nella struttura {W: pieces, B: pieces}
    :param state:
    :return:
    """
    pieces_w = []
    pieces_b = []
    for index, value in enumerate(state.board):
        if value == 'W':
            pieces_w.append(index)
        if value == 'B':
            pieces_b.append(index)

    return {
        'W': pieces_w,
        'B': pieces_b
    }


def count_all_adjacents_player(board, pieces_player):
    """
    Metodo prende in ingresso tutte le pedine di un giocatore e restituisce il numero di adjacenti vuoti totale
    :param board: 
    :param pieces_player: 
    :return: 
    """
    count_free_adjacent = 0
    for piece in pieces_player:
        adjacent = adjacent_locations(piece)
        for pos in adjacent:
            if board[pos] == 'O':
                count_free_adjacent += 1

    return count_free_adjacent


def check_delete_win(game, state, move):

    state_copy = state
    new_state = game.result(state_copy, move)
    return abs(new_state.utility)


def check_win_or_lose(state, player):
    """
    Controllo se in base allo stato il giocatore passato come parametro vince (allora return 1000),
    perdere (allora return -1000) o non succede niente (allora return 0)
    :param state:
    :param player:
    :return:
    """

    if player == 'W':
        if state.b_board < 3 or (len(can_move(state, 'B')) == 0 and state.b_board > 3):
            return 1000
        elif state.w_board < 3 or (len(can_move(state, 'W')) == 0 and state.w_board > 3):
            return -1000
        else:
            return 0
    else:
        if state.w_board < 3 or (len(can_move(state, 'W')) == 0 and state.w_board > 3):
            return 1000
        elif state.b_board < 3 or (len(can_move(state, 'B')) == 0 and state.b_board > 3):
            return -1000
        else:
            return 0
