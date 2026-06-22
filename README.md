### Hexlet tests and linter status:
[![Actions Status](https://github.com/alexlealch/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alexlealch/python-project-174/actions)

# Gendiff - Configuration File Difference Finder

Gendiff is a CLI tool that compares two configuration files (JSON or YAML) and displays the differences in a clear, human-readable format.

## Installation

```bash
pip install .
```

## Usage

### CLI
Run the tool from the terminal:
```bash
python -m gendiff.scripts.gendiff file1.json file2.json
python -m gendiff.scripts.gendiff file1.yaml file2.yaml
python -m gendiff.scripts.gendiff file1.yml file2.yml
```

### Library
Use `generate_diff` in your Python code:
```python
from gendiff.src.generate_diff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

## Example Output
```
{
  - follow: false
  host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Demo
Check out the tool in action: [https://asciinema.org/a/TzfGcZA8COADhpGg](https://asciinema.org/a/TzfGcZA8COADhpGg)
