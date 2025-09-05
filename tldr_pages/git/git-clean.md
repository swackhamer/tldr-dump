# git-clean

> Remove files not tracked by Git from the working tree. More information: <https://git-scm.com/docs/git-clean>.

## Examples

### Delete untracked files

```bash
git clean
```

### Interactively delete untracked files

```bash
git clean [-i|--interactive]
```

### Show which files would be deleted without actually deleting them

```bash
git clean [-n|--dry-run]
```

### Forcefully delete untracked files

```bash
git clean [-f|--force]
```

### Forcefully delete untracked [d]irectories

```bash
git clean [-f|--force] -d
```

### Delete untracked files, including e[x]cluded files (files ignored in `.gitignore` and `.git/info/exclude`)

```bash
git clean -x
```
