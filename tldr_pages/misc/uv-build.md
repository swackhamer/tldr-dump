# uv-build

> Build Python packages into source distributions and wheels. More information: <https://docs.astral.sh/uv/reference/cli/#uv-build>.

## Examples

### Build a package in the current directory

```bash
uv build
```

### Build a package from a specific directory

```bash
uv build path/to/directory
```

### Build only a wheel (skip source distribution)

```bash
uv build --wheel
```

### Build only a source distribution (skip wheel)

```bash
uv build --sdist
```

### Build and output to a specific directory

```bash
uv build [-o|--out-dir] path/to/output
```

### Build a specific package in a workspace

```bash
uv build --package package_name
```

### Build all packages in the workspace

```bash
uv build [--all|--all-packages]
```

### Build with a specific Python interpreter

```bash
uv build [-p|--python] python3.11
```
