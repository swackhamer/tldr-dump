# uv-version

> Read or update a project's version. More information: <https://docs.astral.sh/uv/reference/cli/#uv-version>.

## Examples

### Display the current project version

```bash
uv version
```

### Set the project version to a specific value

```bash
uv version 1.2.3
```

### Bump the project version using semantic versioning

```bash
uv version --bump major|minor|patch
```

### Preview version changes without writing to `pyproject.toml`

```bash
uv version --bump patch --dry-run
```

### Update version for a specific package in a workspace

```bash
uv version --package package_name 1.2.3
```

### Display version in JSON format

```bash
uv version --output-format json
```
