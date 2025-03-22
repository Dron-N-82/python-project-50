#!usr/bin/env python3
#import argparse
import gendiff.build_diff as diff_nested
import gendiff.parse_file as p_f
from gendiff.formatting import formating_diff
#import gendiff.cli as cli

def generate_diff(file1_path, file2_path, style='stylish'):
    #arg_data = cli.parse_argumet()
    data1 = p_f.get_data_from_file(file1_path)
    data2 = p_f.get_data_from_file(file2_path)
    diff = diff_nested.generate_diff(data1, data2)
    result = formating_diff(diff, style)
    return result
