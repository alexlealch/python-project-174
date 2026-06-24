def stylish_format(diff, depth=0):
    """
    Format the abstract diff tree into a stylish string representation.

    Args:
        diff: The abstract diff tree from calculate_diff (dict with keys
              as field names, values as dicts with 'status', 'old_value',
              'new_value', and optionally 'children')
        depth: Current nesting depth (for indentation)

    Returns:
        Formatted string representing the differences
    """
    # Calculate the indentation for this level: 2 * (depth + 1) spaces
    indent = ' ' * (2 * (depth + 1))
    lines = []
    for key in sorted(diff.keys()):
        value = diff[key]
        status = value['status']

        if status == 'nested':
            # For a nested dictionary, we show the key and then recurse
            lines.append(f"{indent}{key}: {{")
            lines.append(stylish_format(value['children'], depth + 1))
            lines.append(f"{indent}}}")
        elif status == 'added':
            lines.append(f"{indent}+ {key}: {_stringify(value['new_value'])}")
        elif status == 'deleted':
            lines.append(f"{indent}- {key}: {_stringify(value['old_value'])}")
        elif status == 'changed':
            lines.append(f"{indent}- {key}: {_stringify(value['old_value'])}")
            lines.append(f"{indent}+ {key}: {_stringify(value['new_value'])}")
        elif status == 'unchanged':
            lines.append(f"{indent}{key}: {_stringify(value['old_value'])}")

    if depth == 0:
        return f"{{\n{'\n'.join(lines)}\n}}"
    else:
        return '\n'.join(lines)


def _stringify(value):
    """Convert a value to its string representation for display."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)
