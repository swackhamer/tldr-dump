# dvc-checkout

> Checkout data files and directories from cache. More information: <https://dvc.org/doc/command-reference/checkout>.

## Examples

### Checkout the latest version of all target files and directories

```bash
dvc checkout
```

### Checkout the latest version of a specified target

```bash
dvc checkout target
```

### Checkout a specific version of a target from a different Git commit/tag/branch

```bash
git checkout commit_hash|tag|branch target && dvc checkout target
```
