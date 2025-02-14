import json

def parse_json(file_json):
    with open(file_json, 'r') as file:
        data = json.load(file)
    return data

dict1 = parse_json('file1_7.json')
dict2 = parse_json('file2_7.json')


def generate_diff(file1_, file2_):
    res = {}
    def inner(file1_7, file2_7):
        
        keys = sorted(set(file1_7.keys()) | set(file2_7.keys()))

        for key in keys:
            value1 = file1_7.get(key)
            value2 = file2_7.get(key)
            
            if not isinstance(value1, dict) and not isinstance(value2, dict):
            
                if key in file1_7 and key in file2_7:
                    if value1 == value2:
                        res[key] = {"type": "unchanged", "value": value1}
                    if value1 != value2:
                        res[key] = {"type": "changed", "old": value1, 'new': value2}

                if value1 is None:
                    res[key] = {"type": "added", "value": value2}

                if value2 is None:
                    res[key] = {"type": "removed", "value": value1}

            elif isinstance(value1, dict) and isinstance(value2, dict):
#            else:
                nested_diff = inner(value1, value2)
                if nested_diff:
                    res[key] = {"type": "added", "value": {"type": "added", "value": nested_diff}}
           
        return (res)
    return inner(file1_, file2_)

print(generate_diff(dict1, dict2))