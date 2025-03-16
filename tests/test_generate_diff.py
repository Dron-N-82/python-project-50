from gendiff.generate_diff import generate_diff


# def test_gennerate_diff():
#     comparison = 'tests/test_data/test_json.txt'
#     file1 = 'tests/test_data/file1.json'
#     file2 = 'tests/test_data/file2.json'

#     with open(comparison,'r') as txt:
#         text = ''.join(txt.readlines())

#     gd_text = generate_diff(file1, file2)

#     assert gd_text == text


# def test_gennerate_diff():
#     comparison = 'tests/test_data/test_yaml.txt'
#     file1 = 'tests/test_data/file1.yaml'
#     file2 = 'tests/test_data/file2.yaml'

#     with open(comparison,'r') as txt:
#         text = ''.join(txt.readlines())

#     gd_text = generate_diff(file1, file2)

#     assert gd_text == text


def test_gennerate_diff():
    comparison = 'tests/test_data/test_json_7.txt'
    file1 = 'tests/test_data/file1_7.json'
    file2 = 'tests/test_data/file2_7.json'
    style = 'stylish'
    
    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff(file1, file2, style)

    assert gd_text == text


def test_gennerate_diff():
    comparison = 'tests/test_data/test_yaml_7.txt'
    file1 = 'tests/test_data/file1_7.yaml'
    file2 = 'tests/test_data/file2_7.yaml'
    style = 'stylish'

    with open(comparison,'r') as txt:
        text = ''.join(txt.readlines())

    gd_text = generate_diff(file1, file2, style)

    assert gd_text == text