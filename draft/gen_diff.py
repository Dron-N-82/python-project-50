import json

def parse_json(file_json):
    with open(file_json, 'r') as file:
        data = json.load(file)
    return data

#print()
#print(parse_json('file11.json'))
#print()
#print(parse_json('file22.json'))
#print()
file1 = parse_json('file11.json')
file2 = parse_json('file22.json')


def generate_diff(file1_, file2_):
#    res = {}
    def iner_(file1_7, file2_7):
        keys = sorted(file1_7.keys() | file2_7.keys())
        res = {}
        for key in keys:
            if key in file1_7 and key not in file2_7:
                if not isinstance(file1_7.get(key), dict):
                    res[key] = {"type": "removed", "value": file1_7.get(key)}
                else:
                    iner_(file1_7.get(key), file2_7.get(key))
            elif key in file2_7 and key not in file1_7:
                if not isinstance(file2_7.get(key), dict):
                    res[key] = {"type": "added", "value": file2_7.get(key)}
                else:
                     iner_(file1_7.get(key), file2_7.get(key))
            elif key in file1_7 and file2_7:
                res[key] = {"type": "unchanged", "value": file1_7.get(key)}
            
        return (res)
    return iner_(file1_, file2_)

print(generate_diff(file1, file2))