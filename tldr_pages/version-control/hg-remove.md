# hg-remove

> Remove specified files from the staging area. More information: <https://www.mercurial-scm.org/help/commands/remove>.

## Examples

### Remove files or directories from the staging area

```bash
hg remove path/to/file
```

### Remove all staged files matching a specified pattern

```bash
hg remove [-I|--include] pattern
```

### Remove all staged files, excluding those that match a specified pattern

```bash
hg remove [-X|--exclude] pattern
```

### Recursively remove sub-repositories

```bash
hg remove [-S|--subrepos]
```

### Remove files from the repository that have been physically removed

```bash
hg remove [-A|--after]
```
