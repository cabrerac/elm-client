import sys
import logging
from datetime import datetime
from util import util
import os


url = 'http://127.0.0.1:5000/'

def main(config_file_name):

    # create and configure logger
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    # console log
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # set the level for console output
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    # file log
    if not os.path.exists('./logs/'):
        os.makedirs('./logs/')
    log_file = './logs/elm_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)  # set the level for file output
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # reading task configuration
    step = 1
    logger.info(str(step) + '. Reading task configuration...')
    model, method, data_path = util.read_task_config(config_file_name)

    # writing task configuration
    step = step + 1
    logger.info(str(step) + '. Requesting estimator for task...')
    task_id = util.submit_task_config(url + 'estimate', model, method, data_path)

    # wait for process or exit
    if task_id is not None:
        step = step + 1
        logger.info(str(step) + '. Waiting for the parameters estimation to finish...')

    # process finished
    logger.info('Process finished.')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Please provide the configuration file path in the correct format...')
