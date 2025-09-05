# git-diff

> Show changes to tracked files. More information: <https://git-scm.com/docs/git-diff>.

## Examples

### Show unstaged changes

```bash
git diff
```

### Show all uncommitted changes (including staged ones)

```bash
git diff HEAD
```

### Show only staged (added, but not yet committed) changes

```bash
git diff --staged
```

### Show changes from all commits since a given date/time (a date expression, e.g. "1 week 2 days" or an ISO date)

```bash
git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'
```

### Show diff statistics, like files changed, histogram, and total line insertions/deletions

```bash
git diff --stat commit
```

### Output a summary of file creations, renames and mode changes since a given commit

```bash
git diff --summary commit
```

### Compare a single file between two branches or commits

```bash
git diff branch_1..branch_2 path/to/file
```

### Compare different files from the current branch to another branch

```bash
git diff other_branch:path/to/file2 path/to/file1
```
