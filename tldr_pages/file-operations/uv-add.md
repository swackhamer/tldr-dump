# uv-add

> Add package dependencies to the `pyproject.toml` file. Packages are specified according to <https://peps.python.org/pep-0508/>. More information: <https://docs.astral.sh/uv/reference/cli/#uv-add>.

## Examples

### Add the latest version of a package

```bash
uv add package
```

### Add multiple packages

```bash
uv add package1 package2 ...
```

### Add a package with a version requirement

```bash
uv add package>=1.2.3
```

### Add packages to an optional dependency group, which will be included when published

```bash
uv add --optional optional package1 package2 ...
```

### Add packages to a local group, which will not be included when published

```bash
uv add --group group package1 package2 ...
```

### Add packages to the dev group, shorthand for `--group dev`

```bash
uv add --dev package1 package2 ...
```

### Add package as editable

```bash
uv add --editable path/to/package/
```

### Enable an extra when installing package, may be provided multiple times

```bash
uv add package --extra extra_feature
```
