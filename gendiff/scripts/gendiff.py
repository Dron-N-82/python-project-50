#!/usr/bin/env python3
from gendiff.cli import parse_argumet
from gendiff.generate_diff import generate_diff


def main():
    args = parse_argumet()
    file1_path = args['first_file']
    file2_path = args['second_file']
    format = args['-f, --format']
    diff = generate_diff(file1_path, file2_path, format)
    print(diff)


if __name__ == '__main__':
    main()