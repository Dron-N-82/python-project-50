import argparse
import json

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
        'format': args.format
    }
# Читаем и получаем данные из *.json файла
def get_data_from_file(file_json):
    with open(file_json) as handle_file:
        data = json.load(handle_file)
    return data


def maindiff():
    arg_data = parse_argumet()
    first = get_data_from_file(arg_data['first_file'])
    second = get_data_from_file(arg_data['second_file'])
    
