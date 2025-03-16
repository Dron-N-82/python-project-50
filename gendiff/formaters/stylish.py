import itertools


def convert_stylish(value, replacer=' ', spaces_count=4):
    '''
                Синтаксис:

        convert_stylish(dict[, replacer[, spaces_count]])

        Параметры:

            - dict
                - Значение, преобразуемое в строку.
            - replacer, необязательный
                - Строка – отступ для ключа; Значение по умолчанию – один пробел.
            - spaces_count, необязательный
                - Число – количество повторов отступа ключа в зависимости от вложенности.
                  Значение по умолчанию – 1
        '''
    

    def format_value(value, deep_indent):
        if isinstance(value, dict):
            values = [
                f"{deep_indent}    {k}: {format_value(v, deep_indent + replacer*spaces_count)}"
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
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for k in current_dict:
            key = 'type'
            nodetype = current_dict[k][key]
            if nodetype == 'nested':
                сhild = iter_(current_dict[k]['child'], deep_indent_size)
                lines.append(f'{deep_indent[:-2]}  {k}: {сhild}')
            elif nodetype == 'added':
                new_value = format_value(current_dict[k]['new_value'], deep_indent)
                lines.append(f'{deep_indent[:-2]}+ {k}: {new_value}')
            elif nodetype == 'removed':
                old_val = format_value(current_dict[k]['old_value'], deep_indent)
                lines.append(f'{deep_indent[:-2]}- {k}: {old_val}')
            elif nodetype == 'changed':
                old = format_value(current_dict[k]['value']['old_value'], deep_indent)
                new = format_value(current_dict[k]['value']['new_value'], deep_indent)
                lines.append(f'{deep_indent[:-2]}- {k}: {old}')
                lines.append(f'{deep_indent[:-2]}+ {k}: {new}')
            elif nodetype == 'unchanged':
                value = current_dict[k]['value']
                lines.append(f'{deep_indent[:-2]}  {k}: {value}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
