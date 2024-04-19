import yaml


def read_task_config(config_file_name):
    with open(config_file_name) as file:
        config_file = yaml.load(file, Loader=yaml.FullLoader)

    model = ''
    if 'model' in config_file:
        model = config_file['model']

    estimator = ''
    if 'estimator' in config_file:
        estimator = config_file['estimator']

    data_path = ''
    if 'data_path' in config_file:
        data_path = config_file['data_path']

    return model, estimator, data_path
