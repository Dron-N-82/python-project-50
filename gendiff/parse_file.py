import json

import yaml


def parse_data(data, extension):
    if extension == '.json':
        return json.loads(data)
    elif extension == '.yml' or '.yaml':
        return yaml.load(data, Loader=yaml.FullLoader)
    else:
        raise ValueError(f"Unsupported format: {extension}")
