import sys
import logging
from datetime import datetime
from data import util
import os


def main(config_file_name):

    # Create and configure logger
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    # Console log
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set the level for console output
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    # File log
    if not os.path.exists('./logs/'):
        os.makedirs('./logs/')
    log_file = './logs/' + config_file_name.replace('.yaml', '_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)  # Set the level for file output
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    step = 1
    # Reading configuration of parametrisation task
    logger.info(str(step) + '. Reading task parameters...')
    model, estimator, data_path = util.read_task_config(config_file_name)
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Please provide the search parameters file path in the correct format...')
