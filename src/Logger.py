
import logging
from datetime import datetime
from os import path

from collections import namedtuple
GameState = namedtuple('GameState', 'to_move, utility, board, moves, w_board, b_board, w_no_board, b_no_board')


class Logger:

    def __init__(self):
        """
        Questo costruttore inizializza le impostazioni per il logger
        """
        self.logger = logging.getLogger('fuff_team_logger')
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        dir_path = path.dirname(__file__)
        root_dir = path.normpath(dir_path + '/..')
        self.log_path = path.normpath(root_dir + '/log')
        self.temp_path = path.normpath(self.log_path + '/tmp-state')

    def init_log_file(self):
        """
        Inizializza il file del log creando un file con un time stamp diverso ogni volta
        :return:
        """
        now = get_current_time()
        log_path_file = path.normpath(self.log_path + '/' + str(now) + '.log')
        logging.basicConfig(filename=log_path_file, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def info_message(self, message):
        """
        Scrive il messaggio passato nel file del log inizializzato nella init_log_file
        :param message:
        :return:
        """
        self.logger.info(str(message))

    def save_state(self, state, file_name=None):
        """
        Salva su un file lo stato che gli passiamo come parametro
        :param state:
        :param file_name:
        :return:
        """

        state_items = []
        for key in state._fields:
            state_items.append(getattr(state, key))

        file_name = file_name or 'state.txt'

        temp_path_file = path.normpath(self.temp_path + '/' + file_name)
        out_file = open(temp_path_file, 'w+')

        for item in state_items:
            out_file.write(str(str(item) + '\n'))

        out_file.close()

    def read_state(self, file_name):
        """
        Legge lo stato che è stato salvato nel file
        :param file_name:
        :return:
        """
        temp_path_file = path.normpath(self.temp_path + '/' + file_name)
        inp_file = open(temp_path_file, 'r+')

        contents = inp_file.read()

        state_elements = contents.split('\n')

        return GameState(
            to_move=str(state_elements[0]),
            utility=int(state_elements[1]),
            board=set_list_items(state_elements[2]),
            moves=set_list_items(state_elements[3], False),
            w_board=int(state_elements[4]),
            b_board=int(state_elements[5]),
            w_no_board=int(state_elements[6]),
            b_no_board=int(state_elements[7])
        )


def set_list_items(string_items, is_string=True):
    string_items = string_items.replace("[", "").replace("]", "")
    all_items = str(string_items).split(',')

    new_list = []
    for item in all_items:
        if is_string:
            new_list.append(str(item).replace("'", '').replace('"', '').strip())
        else:
            new_list.append(int(str(item).replace("'", '').replace('"', '').strip()))

    return new_list


def get_current_time():
    return datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S")