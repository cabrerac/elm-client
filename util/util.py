import yaml
import csv
from clients import client
import json


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

    steps = {}
    if 'steps' in config_file:
        steps = config_file['steps']

    return model, method, data_path, steps


def submit_task_config(url, model, method, data_path, steps):
    with open(data_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
    task_config = {'model': model, 'method': method, 'data': data, 'steps': steps}
    request_response = client.request(url, 'post', task_config, {})
    if request_response.status_code == 200:
        task_id = json.loads(request_response.content)['task_id']
    else:
        task_id = None
    return task_id
