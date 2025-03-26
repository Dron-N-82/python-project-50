from gendiff.generate_diff import generate_diff


def run_test(comparison, file1, file2, style):
    with open(comparison, 'r') as txt:
        text = ''.join(txt.readlines())
    gd_text = generate_diff(file1, file2, style)
    assert gd_text == text


def test_gennerate_diff_json_in_style_stylish():
    run_test(
        'tests/test_data/test_stylish_7.txt',
        'tests/test_data/file1_7.json',
        'tests/test_data/file2_7.json',
        'stylish'
    )
    

def test_gennerate_diff_yaml_in_style_stylish():
    run_test(
        'tests/test_data/test_stylish_7.txt',
        'tests/test_data/file1_7.yaml',
        'tests/test_data/file2_7.yaml',
        'stylish'
    )


def test_gennerate_diff_json_in_style_plain():
    run_test(
        'tests/test_data/test_plain_8.txt',
        'tests/test_data/file1_7.json',
        'tests/test_data/file2_7.json',
        'plain'
    )


def test_gennerate_diff_yaml_in_style_plain():
    run_test(
        'tests/test_data/test_plain_8.txt',
        'tests/test_data/file1_7.yaml',
        'tests/test_data/file2_7.yaml',
        'plain'
    )

    
def test_gennerate_diff_json_in_style_json():
    run_test(
        'tests/test_data/test_json_9.txt',
        'tests/test_data/file1_7.json',
        'tests/test_data/file2_7.json',
        'json'
    )


def test_gennerate_diff_yaml_in_style_json():
    run_test(
        'tests/test_data/test_json_9.txt',
        'tests/test_data/file1_7.yaml',
        'tests/test_data/file2_7.yaml',
        'json'
    )