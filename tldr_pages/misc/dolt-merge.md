# dolt-merge

> Join two or more development histories together. More information: <https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

## Examples

### Incorporate changes from the named commits into the current branch

```bash
dolt merge branch_name
```

### Incorporate changes from the named commits into the current branch without updating the commit history

```bash
dolt merge --squash branch_name
```

### Merge a branch and create a merge commit even when the merge resolves as a fast-forward

```bash
dolt merge --no-ff branch_name
```

### Merge a branch and create a merge commit with a specific commit message

```bash
dolt merge --no-ff [-m|--message] "message" branch_name
```

### Abort the current conflict resolution process

```bash
dolt merge --abort
```
