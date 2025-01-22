import json
import yaml

def parse_json(file_json):
    with open(file_json, 'r') as handle_file:
        data = json.load(handle_file)
    return data


def parse_yaml(file_yaml):
    with open(file_yaml, 'r') as handle_file:
        data = yaml.load(handle_file, Loader=yaml.FullLoader)
    return data