import yaml
import csv
from clients import mongo


def read_task_config(config_file_name):
    with open(config_file_name) as file:
        config_file = yaml.load(file, Loader=yaml.FullLoader)

    model = ''
    if 'model' in config_file:
        model = config_file['model']

    method = ''
    if 'method' in config_file:
        method = config_file['method']

    data_path = ''
    if 'data_path' in config_file:
        data_path = config_file['data_path']

    return model, method, data_path


def write_task_config(model, method, data_path):
    with open(data_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
    task_config = {'model': model, 'method': method, 'data': data}
    task_id = mongo.store('elm', 'tasks', task_config)
    return task_id
