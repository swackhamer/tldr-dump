# pytest

> Run Python tests. More information: <https://docs.pytest.org/en/latest/how-to/usage.html>.

## Examples

### Run tests from specific files

```bash
pytest path/to/test_file1.py path/to/test_file2.py ...
```

### Run tests with names matching a specific [k]eyword expression

```bash
pytest -k expression
```

### Exit as soon as a test fails or encounters an error

```bash
pytest --exitfirst
```

### Run tests matching or excluding markers

```bash
pytest -m marker_name1 and not marker_name2
```

### Run until a test failure, continuing from the last failing test

```bash
pytest --stepwise
```

### Run tests without capturing output

```bash
pytest --capture=no
```
