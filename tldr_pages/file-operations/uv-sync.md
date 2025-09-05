# uv-sync

> Update the project's environment to match the lockfile. More information: <https://docs.astral.sh/uv/reference/cli/#uv-sync>.

## Examples

### Sync the project environment with the lockfile

```bash
uv sync
```

### Sync and include all optional dependencies

```bash
uv sync --all-extras
```

### Sync with specific optional dependencies

```bash
uv sync --extra extra_name
```

### Sync only development dependencies

```bash
uv sync --only-dev
```

### Sync excluding development dependencies

```bash
uv sync --no-dev
```

### Sync specific dependency groups

```bash
uv sync --group group_name
```

### Check if environment is already synchronized (no changes)

```bash
uv sync --check
```

### Preview what would be synced without making changes

```bash
uv sync --dry-run
```
