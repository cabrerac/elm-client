import sys
import logging
from datetime import datetime
from util import util
from clients import client
import os
import time
import numpy

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


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
    log_file = './logs/xlm_client_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)  # set the level for file output
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # reading task configuration
    step = 1
    logger.info(str(step) + '. Reading task configuration...')
    model, method, steps, metadata, seed = util.read_task_config(config_file_name)

    # writing task configuration
    step = step + 1
    logger.info(str(step) + '. Reading data for task...')
    data = util.generate_data(seed)

    linear_model = LinearRegression()
    linear_model.fit(numpy.array(data['x']['train']).reshape(-1, 1), numpy.array(data['y']['train']).reshape(-1, 1))
    print('b1=' + str(linear_model.coef_))
    print('b0=' + str(linear_model.intercept_))
    y_pred = linear_model.predict(numpy.array(data['x']['test']).reshape(-1, 1))
    print('y_pred=' + str(y_pred))
    mse = mean_squared_error(numpy.array(data['y']['test']).reshape(-1, 1), y_pred)
    print('mse=' + str(mse))
    r2 = r2_score(numpy.array(data['y']['test']).reshape(-1, 1), y_pred)
    print('r2=' + str(r2))
    step = step + 1
    logger.info(str(step) + '. Requesting learner for task...')
    timestamp = int(time.time()*1000)
    task_id = 'task_' + str(timestamp)
    res = client.submit_task_config(url + 'learn', task_id, model, method, steps, metadata, data)

    # wait for process or exit
    if res == 200:
        step = step + 1
        logger.info(str(step) + '. Waiting for the learning process to finish...')

    # process finished
    logger.info('Process finished.')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Please provide the configuration file path in the correct format...')
