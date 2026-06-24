import json
import yaml
import os


def load_file(filepath):
    """Load file based on its extension (.json, .yml, .yaml)"""
    _, extension = os.path.splitext(filepath)
    with open(filepath, 'r') as f:
        if extension.lower() in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        elif extension.lower() == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {extension}")


def _stringify(value):
    """Convert a value to its string representation for display."""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)
