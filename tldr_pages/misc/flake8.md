# flake8

> Check the style and quality of Python code. More information: <https://flake8.pycqa.org/en/latest/user/options.html>.

## Examples

### Lint a file or directory recursively

```bash
flake8 path/to/file_or_directory
```

### Lint a file or directory recursively and show the line on which each error occurred

```bash
flake8 --show-source path/to/file_or_directory
```

### Lint a file or directory recursively and ignore a list of rules. (All available rules can be found at <https://www.flake8rules.com/>)

```bash
flake8 --ignore rule1,rule2,... path/to/file_or_directory
```

### Lint a file or directory recursively but exclude files matching the given globs or substrings

```bash
flake8 --exclude substring1,glob2 path/to/file_or_directory
```
