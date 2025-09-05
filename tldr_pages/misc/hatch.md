# hatch

> Modern, extensible Python project manager. See also: `poetry`. More information: <https://hatch.pypa.io/latest/cli/reference/>.

## Examples

### Create a new Hatch project

```bash
hatch new project_name
```

### Initialize Hatch for an existing project

```bash
hatch new --init
```

### Build a Hatch project

```bash
hatch build
```

### Remove build artifacts

```bash
hatch clean
```

### Create a default environment with dependencies defined in the `pyproject.toml` file

```bash
hatch env create
```

### Show environment dependencies as a table

```bash
hatch dep show table
```
