# pylint

> A Python code linter. More information: <https://pylint.pycqa.org/en/latest/>.

## Examples

### Show lint errors in a file

```bash
pylint path/to/file.py
```

### Lint a package or module (must be importable; no `.py` suffix)

```bash
pylint package_or_module
```

### Lint a package from a directory path (must contain an `__init__.py` file)

```bash
pylint path/to/directory
```

### Lint a file and use a configuration file (usually named `pylintrc`)

```bash
pylint --rcfile path/to/pylintrc path/to/file.py
```

### Lint a file and disable a specific error code

```bash
pylint --disable C,W,no-error,design path/to/file
```
