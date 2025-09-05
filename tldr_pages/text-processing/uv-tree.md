# uv-tree

> Display project dependencies in a tree format. More information: <https://docs.astral.sh/uv/reference/cli/#uv-tree>.

## Examples

### Show dependency tree for current environment

```bash
uv tree
```

### Show dependency tree for all environments

```bash
uv tree --universal
```

### Show dependency tree up to a certain depth

```bash
uv tree [-d|--depth] n
```

### Show the latest available version for all outdated packages

```bash
uv tree --outdated
```

### Exclude dependencies from the dev group

```bash
uv tree --no-dev
```

### Show the inverted tree, so children are dependents instead of dependencies

```bash
uv tree --invert
```
