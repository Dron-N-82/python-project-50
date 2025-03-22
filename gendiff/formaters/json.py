import json


def convert_json(diff):
    result = json.dumps(diff, indent=4)
    return result