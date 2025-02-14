import json

def parse_json(file_json):
    with open(file_json, 'r') as file:
        data = json.load(file)
    return data

dict1 = parse_json('file11.json')
dict2 = parse_json('file22.json')


def generate_diff(file1_, file2_):
    res = {}
    def inner(file1_7, file2_7):
        
        keys = sorted(set(file1_7.keys()) | set(file2_7.keys()))

        for key in keys:
            value1 = file1_7.get(key)
            value2 = file2_7.get(key)

            if key not in file1_7 and key in file2_7:
                res[key] = {"type": "added", "value": value2}

            elif key in file1_7 and key not in file2_7:
                res[key] = {"type": "removed", "value": value1}

            elif key in file1_7 and key in file2_7:
                if value1 == value2:
                    res[key] = {"type": "unchanged", "value": value1}
                if value1 != value2:
                    res[key] = {"type": "changed", "old": value1, 'new': value2}

            else:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    nested_diff = inner(value1, value2)
                if nested_diff:
                    res[key] = {"type": "nested", "value": nested_diff}
                  
        return (res)
    return inner(file1_, file2_)

print(generate_diff(dict1, dict2))