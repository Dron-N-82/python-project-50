def build_diff(dict1_, dict2_):

    res = {}
    keys = sorted(set(dict1_.keys()) | set(dict2_.keys()))

    for key in keys:
        value1 = dict1_.get(key)
        value2 = dict2_.get(key)

        if key not in dict2_:
            res[key] = {'type': 'removed', 'old_value': value1}
        elif key not in dict1_:
            res[key] = {'type': 'added', 'new_value': value2}
        elif value1 == value2:
            res[key] = {"type": "unchanged", "value": value1}
        elif isinstance(value1, dict) and isinstance(value2, dict):
                nested_diff = build_diff(value1, value2)
                res[key] = {"type": "nested", "child": nested_diff}
        else:
            res[key] = {"type": "changed", "value": {"old_value": value1, 'new_value': value2}}

    return (res)
