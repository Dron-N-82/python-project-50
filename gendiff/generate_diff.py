#!usr/bin/env python3
from gendiff.build_tree import build_diff
import gendiff.parse_file as p_f
from gendiff.formatting import formating_diff


def generate_diff(file1_path, file2_path, style='stylish'):
    data1 = p_f.get_data_from_file(file1_path)
    data2 = p_f.get_data_from_file(file2_path)
    diff = build_diff(data1, data2)
    result = formating_diff(diff, style)
    return result
