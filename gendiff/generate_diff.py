#!usr/bin/env python3
import argparse
import gendiff.diff_nested_dicts as diff_nested
import gendiff.parse_file as p_f
from gendiff.formatting import formating_diff

def parse_argumet():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        epilog='set format of output')
    # Добавляем аргументы
    parser.add_argument('first_file', help='First file to compare.')
    parser.add_argument('second_file', help='Second file to compare.')
    parser.add_argument('-f', '--format')
    # Обрабатываем аргументы
    args = parser.parse_args()

    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        '-f, --format':  args.format
        }

def maindiff():
    arg_data = parse_argumet()
    result = diff_nested.generate_diff(
        p_f.get_data_from_file(arg_data['first_file']),
        p_f.get_data_from_file(arg_data['second_file']),
        )
    print(formating_diff(result, format="stylish"))
