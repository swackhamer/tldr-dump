# pypy

> Fast and compliant alternative implementation of the Python language. More information: <https://doc.pypy.org>.

## Examples

### Start a REPL (interactive shell)

```bash
pypy
```

### Execute script in a given Python file

```bash
pypy path/to/file.py
```

### Execute script as part of an interactive shell

```bash
pypy -i path/to/file.py
```

### Execute a Python expression

```bash
pypy -c "expression"
```

### Run library module as a script (terminates option list)

```bash
pypy -m module arguments
```

### Install a package using pip

```bash
pypy -m pip install package
```

### Interactively debug a Python script

```bash
pypy -m pdb path/to/file.py
```
