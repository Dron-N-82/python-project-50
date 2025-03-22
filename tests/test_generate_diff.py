from gendiff.generate_diff import generate_diff

def test_gennerate_diff():
    comparison = 'tests/test_data/test_stylish_7.txt'
    file1 = 'tests/test_data/file1_7.json'
    file2 = 'tests/test_data/file2_7.json'
    style = 'stylish'
    
    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff(file1, file2, style)

    assert gd_text == text


def test_gennerate_diff():
    comparison = 'tests/test_data/test_stylish_7.txt'
    file1 = 'tests/test_data/file1_7.yaml'
    file2 = 'tests/test_data/file2_7.yaml'
    style = 'stylish'

    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff(file1, file2, style)

    assert gd_text == text


def test_gennerate_diff():
    comparison = 'tests/test_data/test_plain_8.txt'
    file1 = 'tests/test_data/file1_7.json'
    file2 = 'tests/test_data/file2_7.json'
    style = 'plain'

    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff(file1, file2, style)

    assert gd_text == text


def test_gennerate_diff():
    comparison = 'tests/test_data/test_plain_8.txt'
    file1 = 'tests/test_data/file1_7.yaml'
    file2 = 'tests/test_data/file2_7.yaml'
    style = 'plain'

    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff(file1, file2, style)

    assert gd_text == text