# git-revert

> Create new commits which reverse the effect of earlier ones. More information: <https://git-scm.com/docs/git-revert>.

## Examples

### Revert the most recent commit

```bash
git revert HEAD
```

### Revert the 5th last commit

```bash
git revert HEAD~4
```

### Revert a specific commit

```bash
git revert 0c01a9
```

### Revert multiple commits

```bash
git revert branch_name~5..branch_name~2
```

### Don't create new commits, just change the working tree

```bash
git revert [-n|--no-commit] 0c01a9..9a1743
```

### Cancel a Git revert after a merge conflict

```bash
git revert --abort
```
