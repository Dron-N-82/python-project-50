def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def convert_plain(diff, path=''):
    message = []
    for item in diff:
        full_path = f"{path}.{item}" if path else item
        status = diff[item]['type']

        if status == 'nested':
            child = diff[item]['child']
            message.extend(convert_plain(child, full_path))
        elif status == 'added':
            new_value = format_value(diff[item]['new_value'])
            line = (
                f"Property '{full_path}' was added with value: "
                f"{new_value}"
            )
            message.append(line)
        elif status == 'removed':
            line = f"Property '{full_path}' was removed"
            message.append(line)
        elif status == 'changed':
            old = format_value(diff[item]['value']['old_value'])
            new = format_value(diff[item]['value']['new_value'])
            line = (
                f"Property '{full_path}' was updated. From "
                f"{old} to {new}"
            )
            message.append(line)

    return (message)

def convert_to_plain(diff):
    messages = convert_plain(diff)
    return "\n".join(messages)
