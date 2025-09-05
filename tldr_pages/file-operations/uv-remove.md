# uv-remove

> Remove dependencies from the project's `pyproject.toml` file. More information: <https://docs.astral.sh/uv/reference/cli/#uv-remove>.

## Examples

### Remove a dependency from the project

```bash
uv remove package
```

### Remove multiple dependencies

```bash
uv remove package1 package2 ...
```

### Remove a development dependency

```bash
uv remove --dev package
```

### Remove a dependency from an optional dependency group

```bash
uv remove --optional extra_name package
```

### Remove a dependency from a specific dependency group

```bash
uv remove --group group_name package
```

### Remove without syncing the virtual environment

```bash
uv remove --no-sync package
```
