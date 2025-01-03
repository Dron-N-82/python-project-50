#!/usr/bin/env python3

import argparse

def main():
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
    
    

if __name__ == '__main__':
    main()