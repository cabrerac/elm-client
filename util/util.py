import yaml
import numpy as np
from sklearn.model_selection import train_test_split


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

    seed = ''
    if 'seed' in config_file:
        seed = config_file['seed']

    return model, method, steps, metadata, seed


def generate_data(seed):
    np.random.seed(seed)
    x = 2 * np.random.rand(100, 1)
    y = 4 + 3 * x + np.random.rand(100, 1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    data = {'x': {'train': [], 'test': []}, 'y': {'train': [], 'test': []}}
    data['x']['train'] = x_train.flatten().tolist()
    data['x']['test'] = x_test.flatten().tolist()
    data['y']['train'] = y_train.flatten().tolist()
    data['y']['test'] = y_test.flatten().tolist()
    return data
