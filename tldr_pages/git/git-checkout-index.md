# git-checkout-index

> Copy files from the index to the working tree. More information: <https://git-scm.com/docs/git-checkout-index>.

## Examples

### Restore any files deleted since the last commit

```bash
git checkout-index [-a|--all]
```

### Restore any files deleted or changed since the last commit

```bash
git checkout-index [-a|--all] [-f|--force]
```

### Restore any files changed since the last commit, ignoring any files that were deleted

```bash
git checkout-index [-a|--all] [-f|--force] [-n|--no-create]
```

### Export a copy of the entire tree at the last commit to the specified directory (the trailing slash is important)

```bash
git checkout-index [-a|--all] [-f|--force] --prefix path/to/export_directory/
```
