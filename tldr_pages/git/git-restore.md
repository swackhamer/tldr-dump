# git-restore

> Restore working tree files. Requires Git version 2.23+. See also: `git checkout`, `git reset`. More information: <https://git-scm.com/docs/git-restore>.

## Examples

### Restore an unstaged file to the staged version

```bash
git restore path/to/file
```

### Restore an unstaged file to the version of a specific commit

```bash
git restore [-s|--source] commit path/to/file
```

### Discard all unstaged changes to tracked files

```bash
git restore :/
```

### Unstage a file

```bash
git restore [-S|--staged] path/to/file
```

### Unstage all files

```bash
git restore [-S|--staged] :/
```

### Discard all changes to files, both staged and unstaged

```bash
git restore [-W|--worktree] [-S|--staged] :/
```

### Interactively select sections of files to restore

```bash
git restore [-p|--patch]
```
