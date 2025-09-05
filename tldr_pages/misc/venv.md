# venv

> Create lightweight virtual environments in python. More information: <https://docs.python.org/library/venv.html>.

## Examples

### Create a Python virtual environment

```bash
python -m venv path/to/virtual_environment
```

### Activate the virtual environment (Linux and macOS)

```bash
source path/to/virtual_environment/bin/activate
```

### Activate the virtual environment (Windows)

```bash
path\to\virtual_environment\Scripts\activate.bat
```

### Deactivate the virtual environment

```bash
deactivate
```

### Create an alias that generates a `venv` folder and automatically activates it

```bash
alias venv='python -m venv .venv && source .venv/bin/activate|.venv\Scripts\activate.bat'
```
