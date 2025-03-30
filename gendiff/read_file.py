def read_data_from_file(path):
    with open(path, 'r') as handle_file:
        content = handle_file.read()
        return content
