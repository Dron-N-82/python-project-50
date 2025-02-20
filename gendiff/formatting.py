from gendiff.formaters.stylish import convert_stylish

def formating_diff(diff, format):
    if format == 'stylish':
        return convert_stylish(diff)
