def generate_diff(dict1_, dict2_):

    res = {}
    keys = sorted(set(dict1_.keys()) | set(dict2_.keys()))

    for key in keys:
        value1 = dict1_.get(key)
        value2 = dict2_.get(key)

        if key not in dict1_:
            if isinstance(value2, dict):
                res[key] = {"type": "added", "value": generate_diff(value2, value2)}
            else:
                res[key] = {"type": "added", "value": value2}

        elif key not in dict2_:
            res[key] = {"type": "removed", "value": value1}

        elif isinstance(value1, dict) and isinstance(value2, dict):
            nested_diff = generate_diff(value1, value2)
            res[key] = {"type": "nested", "value": nested_diff}

        elif value1 != value2:
            res[key] = {"type": "changed", "value": {"old": value1, 'new': value2}}
                
        else:
            res[key] = {"type": "unchanged", "value": value1}
            
    
    return (res)
