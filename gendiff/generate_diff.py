#!usr/bin/env python3
#import argparse
import gendiff.build_diff as diff_nested
import gendiff.parse_file as p_f
from gendiff.formatting import formating_diff
import gendiff.cli as cli

# def parse_argumet():
#     # Создаем парсер аргументов
#     parser = argparse.ArgumentParser(
#         description='Compares two configuration files and shows a difference.',
#         epilog='set format of output')
#     # Добавляем аргументы
#     parser.add_argument('first_file', help='First file to compare.')
#     parser.add_argument('second_file', help='Second file to compare.')
#     parser.add_argument('-f', '--format')
#     # Обрабатываем аргументы
#     args = parser.parse_args()

#     return {
#         'first_file': args.first_file,
#         'second_file': args.second_file,
#         '-f, --format':  args.format
#         }

def generate_diff(file1_path, file2_path, style='stylish'):
    #arg_data = cli.parse_argumet()
    data1 = p_f.get_data_from_file(file1_path)
    data2 = p_f.get_data_from_file(file2_path)
    diff = diff_nested.generate_diff(data1, data2)
    result = formating_diff(diff, style)
    return result
    #print(f'gendiff {file1_path} {file2_path}\n{formating_diff(result, format="stylish")}')
