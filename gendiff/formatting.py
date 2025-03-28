from gendiff.formaters.json import convert_json
from gendiff.formaters.plain import convert_plain
from gendiff.formaters.stylish import convert_stylish


def formating_diff(diff, format):
    if format == 'stylish':
        return convert_stylish(diff)
    elif format == 'plain':
        return convert_plain(diff)
    elif format == 'json':
        return convert_json(diff)