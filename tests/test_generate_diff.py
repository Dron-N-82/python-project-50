import pytest
from gendiff.generate_diff import generate_diff


def run_test(diff):
    with open(diff, 'r') as test_text:
        return test_text.read()
    

@pytest.mark.parametrize(
    "diff, file1, file2, style",
    [
        (
            'tests/test_data/test_stylish_7.txt',
            'tests/test_data/file1_7.json',
            'tests/test_data/file2_7.json',
            'stylish',
        ),
        (
            'tests/test_data/test_stylish_7.txt',
            'tests/test_data/file1_7.yaml',
            'tests/test_data/file2_7.yaml',
            'stylish',
        ),
        (
            'tests/test_data/test_plain_8.txt',
            'tests/test_data/file1_7.json',
            'tests/test_data/file2_7.json',
            'plain',
        ),
        (
            'tests/test_data/test_plain_8.txt',
            'tests/test_data/file1_7.yaml',
            'tests/test_data/file2_7.yaml',
            'plain',
        ),
        (
            'tests/test_data/test_json_9.txt',
            'tests/test_data/file1_7.json',
            'tests/test_data/file2_7.json',
            'json',
        ),
        (
            'tests/test_data/test_json_9.txt',
            'tests/test_data/file1_7.yaml',
            'tests/test_data/file2_7.yaml',
            'json',
        ),
    ],
)

def test_generate_diff(diff, file1, file2, style):
    diff_text = generate_diff(file1, file2, style)
    test_data = run_test(diff)
    assert diff_text == test_data