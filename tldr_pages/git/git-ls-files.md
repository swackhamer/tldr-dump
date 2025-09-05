# git-ls-files

> Show information about files in the index and the working tree. More information: <https://git-scm.com/docs/git-ls-files>.

## Examples

### Show deleted files

```bash
git ls-files [-d|--deleted]
```

### Show modified and deleted files

```bash
git ls-files [-m|--modified]
```

### Show ignored and untracked files

```bash
git ls-files [-o|--others]
```

### Show untracked files, not ignored

```bash
git ls-files [-o|--others] --exclude-standard
```
