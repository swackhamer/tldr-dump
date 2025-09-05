# git-diff-files

> Compare files using their sha1 hashes and modes. More information: <https://git-scm.com/docs/git-diff-files>.

## Examples

### Compare all changed files

```bash
git diff-files
```

### Compare only specified files

```bash
git diff-files path/to/file
```

### Show only the names of changed files

```bash
git diff-files --name-only
```

### Output a summary of extended header information

```bash
git diff-files --summary
```
