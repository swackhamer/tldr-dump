# git-merge

> Merge branches. More information: <https://git-scm.com/docs/git-merge>.

## Examples

### Merge a branch into your current branch

```bash
git merge branch_name
```

### Edit the merge message

```bash
git merge [-e|--edit] branch_name
```

### Merge a branch and create a merge commit

```bash
git merge --no-ff branch_name
```

### Abort a merge in case of conflicts

```bash
git merge --abort
```

### Merge using a specific strategy

```bash
git merge [-s|--strategy] strategy [-X|--strategy-option] strategy_option branch_name
```
