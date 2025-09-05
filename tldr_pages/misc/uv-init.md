# uv-init

> Create a new Python project. More information: <https://docs.astral.sh/uv/reference/cli/#uv-init>.

## Examples

### Initialize a project in the current directory

```bash
uv init
```

### Initialize a project with a certain name

```bash
uv init project_name
```

### Create a project in a given directory

```bash
uv init --directory path/to/directory project_name
```

### Create a project for a Python library

```bash
uv init [--lib|--library] project_name
```

### Specify the build system

```bash
uv init --build-backend build_backend project_name
```

### Only create a `pyproject.toml`

```bash
uv init --bare project_name
```

### Set the project description

```bash
uv init --description "description" project_name
```
