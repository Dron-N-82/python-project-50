import json
import os

import yaml


def parse_data(file_path, extension):
    with open(file_path, 'r') as handle_file:
        if extension == '.json':
            return json.load(handle_file)
        elif extension == 'yml' or 'yaml':
            return yaml.load(handle_file, Loader=yaml.FullLoader)
        else:
            None


def get_data_from_file(file):
    _, ext = os.path.splitext(file)
    return parse_data(file, ext)
