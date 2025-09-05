# git-show

> Show various types of Git objects (commits, tags, etc.). More information: <https://git-scm.com/docs/git-show>.

## Examples

### Show information about the latest commit (hash, message, changes, and other metadata)

```bash
git show
```

### Show information about a specific commit, tag, or branch (such as `HEAD` for the latest commit)

```bash
git show commit|tag|branch
```

### Show information about the 3rd commit from the HEAD of a branch

```bash
git show branch~3
```

### Show a commit's message in a single line, suppressing the diff output

```bash
git show --oneline [-s|--no-patch] commit
```

### Show only statistics (added/removed characters) about the changed files

```bash
git show --stat commit
```

### Show a simplified list of all files changed in a commit (modified, added, and deleted)

```bash
git show --name-only commit
```

### Show only the list of added, renamed or deleted files

```bash
git show --summary commit
```

### Show the contents of a file as it was at a given revision (e.g. branch, tag or commit)

```bash
git show revision:path/to/file
```
