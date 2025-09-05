# uv

> A fast Python package and project manager. Some subcommands such as `tool` and `python` have their own usage documentation. More information: <https://docs.astral.sh/uv/reference/cli>.

## Examples

### Create a new Python project in the current directory

```bash
uv init
```

### Create a new Python project at the specified path

```bash
uv init path/to/directory
```

### Add a new dependency to the project

```bash
uv add package
```

### Remove a dependency from the project

```bash
uv remove package
```

### Run a script in the project's environment

```bash
uv run path/to/script.py
```

### Run a command in the project's environment

```bash
uv run command
```

### Update a project's environment from `pyproject.toml`

```bash
uv sync
```

### Create a lock file for the project's dependencies

```bash
uv lock
```
