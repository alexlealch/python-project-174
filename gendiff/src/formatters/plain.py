def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain_format(diff):
    def traverse(node, path):
        lines = []
        for key in sorted(node.keys()):
            val = node[key]
            status = val['status']
            current_path = path + [key]
            path_str = '.'.join(current_path)

            if status == 'nested':
                lines.extend(traverse(val['children'], current_path))
            elif status == 'added':
                formatted_val = format_value(val['new_value'])
                lines.append(
                    f"Property '{path_str}' was added with value: "
                    f"{formatted_val}"
                )
            elif status == 'deleted':
                lines.append(f"Property '{path_str}' was removed")
            elif status == 'changed':
                old_val = format_value(val['old_value'])
                new_val = format_value(val['new_value'])
                lines.append(
                    f"Property '{path_str}' was updated. "
                    f"From {old_val} to {new_val}"
                )
            elif status == 'unchanged':
                continue
        return lines

    return '\n'.join(traverse(diff, []))
