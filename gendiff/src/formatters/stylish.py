def stringify(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = ' ' * (4 * (depth + 1))
        closing_indent = ' ' * (4 * depth)
        for key in sorted(value.keys()):
            val = value[key]
            lines.append(f"{indent}{key}: {stringify(val, depth + 1)}")
        return f"{{\n{'\n'.join(lines)}\n{closing_indent}}}"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def stylish_format(diff, depth=1):
    lines = []
    base_indent = ' ' * (4 * depth)
    sign_indent = ' ' * (4 * depth - 2)

    for key in sorted(diff.keys()):
        value = diff[key]
        status = value['status']

        if status == 'nested':
            lines.append(f"{base_indent}{key}: {{")
            lines.append(stylish_format(value['children'], depth + 1))
            lines.append(f"{base_indent}}}")
        elif status == 'added':
            lines.append(
                f"{sign_indent}+ {key}: {stringify(value['new_value'], depth)}"
            )
        elif status == 'deleted':
            lines.append(
                f"{sign_indent}- {key}: {stringify(value['old_value'], depth)}"
            )
        elif status == 'changed':
            lines.append(
                f"{sign_indent}- {key}: {stringify(value['old_value'], depth)}"
            )
            lines.append(
                f"{sign_indent}+ {key}: {stringify(value['new_value'], depth)}"
            )
        elif status == 'unchanged':
            lines.append(
                f"{base_indent}{key}: {stringify(value['old_value'], depth)}"
            )

    if depth == 1:
        return f"{{\n{'\n'.join(lines)}\n}}"
    else:
        return '\n'.join(lines)
