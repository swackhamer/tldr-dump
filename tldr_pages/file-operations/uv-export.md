# uv-export

> Export the project's lockfile to an alternate format. More information: <https://docs.astral.sh/uv/reference/cli/#uv-export>.

## Examples

### Export dependencies to a `requirements.txt` file

```bash
uv export --format requirements-txt [-o|--output-file] requirements.txt
```

### Export dependencies to `pylock.toml` format

```bash
uv export --format pylock.toml
```

### Export only production dependencies (exclude dev dependencies)

```bash
uv export --no-dev
```

### Export including a specific optional dependency group

```bash
uv export --extra group_name
```

### Export including all optional dependencies

```bash
uv export --all-extras
```

### Export including a specific dependency group

```bash
uv export --group group_name
```

### Export without hashes

```bash
uv export --no-hashes
```

### Export dependencies for a specific package in the workspace

```bash
uv export --package package_name
```
