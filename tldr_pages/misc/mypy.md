# mypy

> Type check Python code. More information: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

## Examples

### Type check a specific file

```bash
mypy path/to/file.py
```

### Type check a specific module

```bash
mypy [-m|--module] module_name
```

### Type check a specific package

```bash
mypy [-p|--package] package_name
```

### Type check a string of code

```bash
mypy [-c|--command] "code"
```

### Ignore missing imports

```bash
mypy --ignore-missing-imports path/to/file_or_directory
```

### Show detailed error messages

```bash
mypy [--tb|--show-traceback] path/to/file_or_directory
```

### Specify a custom configuration file

```bash
mypy --config-file path/to/config_file
```

### Display help

```bash
mypy [-h|--help]
```
