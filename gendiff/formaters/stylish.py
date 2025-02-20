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
    def iter_(current_dict, depth):
        if not isinstance(current_dict, dict):
            return str(current_dict)

        deep_indent_size = depth + spaces_count         # deep_indent_size - полный отступ ключа в зависимости от вложенности
        deep_indent = replacer * deep_indent_size       # deep_indent отображение отступа
        current_indent = replacer * depth
        lines = []
        for k in current_dict:
            key = 'type'
            val = current_dict[k]['value']
            if current_dict[k][key] == 'nested':
                lines.append(f'{deep_indent[:-2]}  {k}: {iter_(val, deep_indent_size)}')
            elif current_dict[k][key] == 'added':
                lines.append(f'{deep_indent[:-2]}+ {k}: {iter_(val, deep_indent_size)}')
            elif current_dict[k][key] == 'removed':
                lines.append(f'{deep_indent[:-2]}- {k}: {val}')
            elif current_dict[k][key] == 'changed':
                old = val['old']
                new = val['new']
                lines.append(f'{deep_indent[:-2]}- {k}: {old}')
                lines.append(f'{deep_indent[:-2]}+ {k}: {new}')
            elif current_dict[k][key] == 'unchanged':
                lines.append(f'{deep_indent[:-2]}  {k}: {val}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result) #result
    return iter_(value, 0)

#dict_ = {'common': {'type': 'nested', 'value': {'follow': {'type': 'added', 'value': False}, 'setting1': {'type': 'unchanged', 'value': 'Value 1'}, 'setting2': {'type': 'removed', 'value': 200}, 'setting3': {'type': 'changed', 'value': {'old': True, 'new': None}}, 'setting4': {'type': 'added', 'value': 'blah blah'}, 'setting5': {'type': 'added', 'value': {'key5': {'type': 'unchanged', 'value': 'value5'}}}, 'setting6': {'type': 'nested', 'value': {'doge': {'type': 'nested', 'value': {'wow': {'type': 'changed', 'value': {'old': '', 'new': 'so much'}}}}, 'key': {'type': 'unchanged', 'value': 'value'}, 'ops': {'type': 'added', 'value': 'vops'}}}}}, 'group1': {'type': 'nested', 'value': {'baz': {'type': 'changed', 'value': {'old': 'bas', 'new': 'bars'}}, 'foo': {'type': 'unchanged', 'value': 'bar'}, 'nest': {'type': 'changed', 'value': {'old': {'key': 'value'}, 'new': 'str'}}}}, 'group2': {'type': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'type': 'added', 'value': {'deep': {'type': 'nested', 'value': {'id': {'type': 'nested', 'value': {'number': {'type': 'unchanged', 'value': 45}}}}}, 'fee': {'type': 'unchanged', 'value': 100500}}}}
#dict_ = {'common': {'type': 'nested', 'value': {'follow': {'type': 'added', 'value': False}, 'setting1': {'type': 'unchanged', 'value': 'Value 1'}, 'setting2': {'type': 'removed', 'value': 200}, 'setting3': {'type': 'changed', 'value': {'old': True, 'new': None}}, 'setting4': {'type': 'added', 'value': 'blah blah'}, 'setting5': {'type': 'added', 'value': {'key5': {'type': 'unchanged', 'value': 'value5'}}}, 'setting6': {'type': 'nested', 'value': {'doge': {'type': 'nested', 'value': {'wow': {'type': 'changed', 'value': {'old': '', 'new': 'so much'}}}}, 'key': {'type': 'unchanged', 'value': 'value'}, 'ops': {'type': 'added', 'value': 'vops'}}}}}, 'group1': {'type': 'nested', 'value': {'baz': {'type': 'changed', 'value': {'old': 'bas', 'new': 'bars'}}, 'foo': {'type': 'unchanged', 'value': 'bar'}, 'nest': {'type': 'changed', 'value': {'old': {'key': {'type': 'unchanged', 'value': 'value'}}, 'new': 'str'}}}}, 'group2': {'type': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'type': 'added', 'value': {'deep': {'type': 'nested', 'value': {'id': {'type': 'nested', 'value': {'number': {'type': 'unchanged', 'value': 45}}}}}, 'fee': {'type': 'unchanged', 'value': 100500}}}}

#print(convert_stylish(dict_, replacer=' ', spaces_count=4))