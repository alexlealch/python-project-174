### Hexlet tests and linter status:
[![Actions Status](https://github.com/alexlealch/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alexlealch/python-project-174/actions)
[![Python CI](https://github.com/alexlealch/python-project-174/actions/workflows/pyci.yml/badge.svg)](https://github.com/alexlealch/python-project-174/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alexlealch_python-project-174&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=alexlealch_python-project-174)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=alexlealch_python-project-174&metric=coverage)](https://sonarcloud.io/summary/new_code?id=alexlealch_python-project-174)

# Gendiff - Configuration File Difference Finder

Gendiff is a CLI tool and library that compares two configuration files (JSON or YAML) and displays the differences in a clear, human-readable format. It supports recursive nested comparison and multiple output formats.

## Installation

```bash
pip install .
```

## Usage

### CLI
You can run the tool directly from the terminal after installation:
```bash
gendiff file1.json file2.json
```

Or using poetry:
```bash
poetry run gendiff file1.json file2.json
```

#### Formatting options
By default, `gendiff` uses the `stylish` formatter. You can customize the output format with the `--format` or `-f` option:

* **Stylish** (Default):
  ```bash
  gendiff --format stylish file1.json file2.json
  ```
* **Plain**:
  ```bash
  gendiff --format plain file1.json file2.json
  ```
* **JSON**:
  ```bash
  gendiff --format json file1.json file2.json
  ```

### Library
Use `generate_diff` in your Python code:
```python
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json", format_name="stylish")
print(diff)
```

## Example Outputs

### Stylish format
```
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
    }
}
```

### Plain format
```
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
```

## Demo
Check out the tool in action: [https://asciinema.org/a/7sH9oeJEYosN2BFS](https://asciinema.org/a/7sH9oeJEYosN2BFS)
