# git-branch

> Main Git command for working with branches. More information: <https://git-scm.com/docs/git-branch>.

## Examples

### List all branches (local and remote; the current branch is highlighted by `*`)

```bash
git branch [-a|--all]
```

### List which branches include a specific Git commit in their history

```bash
git branch [-a|--all] --contains commit_hash
```

### Show the name of the current branch

```bash
git branch --show-current
```

### Create new branch based on the current commit

```bash
git branch branch_name
```

### Create new branch based on a specific commit

```bash
git branch branch_name commit_hash
```

### Rename a branch (you must switch to a different branch before doing this)

```bash
git branch [-m|--move] old_branch_name new_branch_name
```

### Delete a local branch (you must switch to a different branch before doing this)

```bash
git branch [-d|--delete] branch_name
```

### Delete a remote branch

```bash
git push remote_name [-d|--delete] remote_branch_name
```
