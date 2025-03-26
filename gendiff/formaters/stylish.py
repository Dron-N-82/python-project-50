import itertools


def format_value(value, deep_indent):
    deep_ind = deep_indent + " " * 4
    if isinstance(value, dict):
        values = [
            f"{deep_indent}    {k}: {format_value(v, deep_ind)}"
            for k, v in value.items()
        ]
        items_str = "\n".join(values)
        return f"{{\n{items_str}\n{deep_indent}}}"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    else:
        return str(value)


def iter_(current_dict, depth):
    deep_indent_size = depth + 4
    deep_indent = " " * deep_indent_size
    current_indent = " " * depth
    lines = []
    for k in current_dict:
        key = 'type'
        nodetype = current_dict[k][key]
        if nodetype == 'nested':
            сhild = iter_(current_dict[k]['child'],
                          deep_indent_size)
            lines.append(f'{deep_indent[:-2]}  {k}: {сhild}')
        elif nodetype == 'added':
            new_value = format_value(current_dict[k]['new_value'],
                                    deep_indent)
            lines.append(f'{deep_indent[:-2]}+ {k}: {new_value}')
        elif nodetype == 'removed':
            old_val = format_value(current_dict[k]['old_value'],
                                   deep_indent)
            lines.append(f'{deep_indent[:-2]}- {k}: {old_val}')
        elif nodetype == 'changed':
            old = format_value(current_dict[k]['value']['old_value'],
                                deep_indent)
            new = format_value(current_dict[k]['value']['new_value'],
                                deep_indent)
            lines.append(f'{deep_indent[:-2]}- {k}: {old}')
            lines.append(f'{deep_indent[:-2]}+ {k}: {new}')
        elif nodetype == 'unchanged':
            value = current_dict[k]['value']
            lines.append(f'{deep_indent[:-2]}  {k}: {value}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def convert_stylish(diff):

    return iter_(diff, depth=0)
