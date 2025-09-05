# uv-lock

> Update the project's lockfile. More information: <https://docs.astral.sh/uv/reference/cli/#uv-lock>.

## Examples

### Create or update the project's lockfile

```bash
uv lock
```

### Check if the lockfile is up-to-date without updating it

```bash
uv lock --check
```

### Assert that a lockfile exists without checking if it's current

```bash
uv lock --check-exists
```

### Preview what would be locked without writing the lockfile

```bash
uv lock --dry-run
```

### Lock a specific Python script instead of the current project

```bash
uv lock --script path/to/script.py
```

### Upgrade all packages to their latest compatible versions

```bash
uv lock --upgrade
```

### Upgrade only specific packages

```bash
uv lock --upgrade-package package1 --upgrade-package package2
```
