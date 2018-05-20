
import logging
from datetime import datetime
from os import path


class Logger:

    def __init__(self):
        self.logger = logging.getLogger('fuff_team_logger')
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def init_log_file(self):
        now = datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S")
        dir_path = path.dirname(__file__)
        log_path = path.normpath(dir_path + '/..')
        log_path = path.normpath(log_path + '/log')
        log_path_file = path.normpath(log_path + '/' + str(now) + '.log')
        logging.basicConfig(filename=log_path_file, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def info_message(self, message):
        self.logger.info(str(message))
