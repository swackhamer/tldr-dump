# uv-cache

> Manage `uv`'s global cache directory. More information: <https://docs.astral.sh/uv/reference/cli/#uv-cache>.

## Examples

### Show the cache directory path

```bash
uv cache dir
```

### Clean the entire cache (removes all cached packages and environments)

```bash
uv cache clean
```

### Clean the cache for specific packages

```bash
uv cache clean package1 package2 ...
```

### Prune all unreachable objects from the cache

```bash
uv cache prune
```

### Prune cache optimized for CI environments like GitHub Actions

```bash
uv cache prune --ci
```

### Use a specific cache directory

```bash
uv cache clean --cache-dir path/to/cache
```

### Clean cache with verbose output

```bash
uv cache clean [-v|--verbose]
```
