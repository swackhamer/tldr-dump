# uv-venv

> Create an isolated Python environment for installing packages. More information: <https://docs.astral.sh/uv/reference/cli/#uv-venv>.

## Examples

### Create a virtual environment in the default location (`.venv`)

```bash
uv venv
```

### Create a virtual environment at a specific path

```bash
uv venv path/to/venv
```

### Create using a specific Python version

```bash
uv venv --python 3.12
```

### Create with a custom prompt prefix

```bash
uv venv --prompt my_project
```

### Create and allow overwriting existing environment

```bash
uv venv --allow-existing venv_name
```
