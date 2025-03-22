import argparse

def parse_argumet():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        epilog='set format of output')
    # Добавляем аргументы
    parser.add_argument('first_file', help='First file to compare.')
    parser.add_argument('second_file', help='Second file to compare.')
    parser.add_argument('-f', '--format',
                        help="set format of output",
                        metavar="FORMAT",
                        default="stylish",
                        choices=["stylish", "plain", "json"],
                        )
    # Обрабатываем аргументы
    args = parser.parse_args()

    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        '-f, --format':  args.format
        }
