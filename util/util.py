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

    steps = {}
    if 'steps' in config_file:
        steps = config_file['steps']

    metadata = {}
    if 'metadata' in config_file:
        metadata = config_file['metadata']

    data_path = ''
    if 'data_path' in config_file:
        data_path = config_file['data_path']

    return model, method, steps, metadata, data_path


def read_data(data_path):
    with open(data_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = {}
        for field_name in csv_reader.fieldnames:
            data[field_name] = []
        for row in csv_reader:
            for key, value in row.items():
                data[key].append(float(value))
    return data
