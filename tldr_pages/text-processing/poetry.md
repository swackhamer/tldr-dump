# poetry

> Manage Python packages and dependencies. See also: `asdf`. More information: <https://python-poetry.org/docs/cli/>.

## Examples

### Create a new Poetry project in the directory with a specific name

```bash
poetry new project_name
```

### Install and add a dependency and its sub-dependencies to the `pyproject.toml` file in the current directory

```bash
poetry add dependency
```

### Install the project dependencies using the `pyproject.toml` file in the current directory

```bash
poetry install
```

### Interactively (append `-n` for non-interactively) initialize the current directory as a new Poetry project

```bash
poetry init
```

### Get the latest version of all dependencies and update `poetry.lock`

```bash
poetry update
```

### Execute a command inside the project's virtual environment

```bash
poetry run command
```

### Bump the version of the project in `pyproject.toml`

```bash
poetry version patch|minor|major|prepatch|preminor|premajor|prerelease
```

### Spawn a shell within the project's virtual environment (for versions below 2.0, use `poetry shell`)

```bash
eval "$(poetry env activate)"
```
