# uv-run

> Run a command or script in the project environment. More information: <https://docs.astral.sh/uv/reference/cli/#uv-run>.

## Examples

### Run a Python script

```bash
uv run path/to/script.py
```

### Run a Python module

```bash
uv run [-m|--module] module_name
```

### Run a command with additional packages installed temporarily

```bash
uv run [-w|--with] package command
```

### Run a script with packages from a requirements file

```bash
uv run --with-requirements path/to/requirements.txt path/to/script.py
```

### Run in an isolated environment (no project dependencies)

```bash
uv run --isolated path/to/script.py
```

### Run without syncing the environment first

```bash
uv run --no-sync command
```
