# uv-self

> Manage the `uv` executable itself. More information: <https://docs.astral.sh/uv/reference/cli/#uv-self>.

## Examples

### Update `uv` to the latest version

```bash
uv self update
```

### Update `uv` to a specific version

```bash
uv self update 0.4.0
```

### Check for available `uv` updates without installing

```bash
uv self update --dry-run
```

### Update `uv` with verbose output

```bash
uv self update [-v|--verbose]
```

### Display the current `uv` version

```bash
uv self version
```

### Display only the version number

```bash
uv self version --short
```

### Display version information in JSON format

```bash
uv self version --output-format json
```
