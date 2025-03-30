#!usr/bin/env python3
import os

from gendiff.build_tree import build_diff
from gendiff.formatting import formating_diff
from gendiff.parse_file import parse_data
from gendiff.read_file import read_data_from_file


def get_data_from_file(full_path):
    _, ext = os.path.splitext(full_path)
    return ext


def generate_diff(path1, path2, style='stylish'):
    data1 = parse_data(read_data_from_file(path1), get_data_from_file(path1))
    data2 = parse_data(read_data_from_file(path2), get_data_from_file(path2))
    diff = build_diff(data1, data2)
    result = formating_diff(diff, style)
    return result
