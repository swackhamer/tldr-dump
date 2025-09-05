# dvc-gc

> Remove unused files and directories from the cache or remote storage. More information: <https://dvc.org/doc/command-reference/gc>.

## Examples

### Garbage collect from the cache, keeping only versions referenced by the current workspace

```bash
dvc gc [-w|--workspace]
```

### Garbage collect from the cache, keeping only versions referenced by branch, tags, and commits

```bash
dvc gc [-a|--all-branches] [-T|--all-tags] [-a|--all-commits]
```

### Garbage collect from the cache, including the default cloud remote storage (if set)

```bash
dvc gc [-a|--all-commits] [-c|--cloud]
```

### Garbage collect from the cache, including a specific cloud remote storage

```bash
dvc gc [-a|--all-commits] [-c|--cloud] [-r|--remote] remote_name
```
