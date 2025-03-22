from gendiff.formaters.stylish import convert_stylish
from gendiff.formaters.plain import convert_to_plain

def formating_diff(diff, format):
    if format == 'stylish':
        return convert_stylish(diff)
    elif format == 'plain':
        return convert_to_plain(diff)
