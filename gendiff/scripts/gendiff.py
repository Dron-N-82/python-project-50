#!/usr/bin/env python3

import argparse

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    
    # Добавляем аргументы
    parser.add_argument('first_file', help='First file to compare.')
    parser.add_argument('second_file', help='Second file to compare.')
    
    # Обрабатываем аргументы
    args = parser.parse_args()
    
    # Здесь будет ваша логика сравнения (пока просто выводим аргументы)
    # print('Сравниваем файлы:')
    # print(f'  {args.first_file}')
    # print(f'  {args.second_file}')

if __name__ == '__main__':
    main()