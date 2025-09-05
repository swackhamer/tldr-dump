# hg-add

> Adds specified files to the staging area for the next commit in Mercurial. More information: <https://www.mercurial-scm.org/help/commands/add>.

## Examples

### Add files or directories to the staging area

```bash
hg add path/to/file
```

### Add all unstaged files matching a specified pattern

```bash
hg add [-I|--include] pattern
```

### Add all unstaged files, excluding those that match a specified pattern

```bash
hg add [-X|--exclude] pattern
```

### Recursively add sub-repositories

```bash
hg add [-S|--subrepos]
```

### Perform a test-run without performing any actions

```bash
hg add [-n|--dry-run]
```
