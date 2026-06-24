from .parsers import load_file
from .core_differ import calculate_diff
from .formatters import stylish_format


def generate_diff(path1, path2, format_name='stylish'):
    """Generates the difference between two configuration files.

    Args:
        path1: Path to first file
        path2: Path to second file
        format_name: Output format (default: 'stylish')

    Returns:
        Formatted string representing the differences
    """
    data1 = load_file(path1)
    data2 = load_file(path2)

    # Calculate the abstract difference tree
    diff_tree = calculate_diff(data1, data2)

    # Format the output based on the requested format
    if format_name == 'stylish':
        return stylish_format(diff_tree)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
