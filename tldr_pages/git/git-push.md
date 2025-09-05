# git-push

> Push commits to a remote repository. More information: <https://git-scm.com/docs/git-push>.

## Examples

### Send local changes in the current branch to its default remote counterpart

```bash
git push
```

### Send changes from a specific local branch to its remote counterpart

```bash
git push remote_name local_branch
```

### Send changes from a specific local branch to its remote counterpart, and set the remote one as the default push/pull target of the local one

```bash
git push [-u|--set-upstream] remote_name local_branch
```

### Send changes from a specific local branch to a specific remote branch

```bash
git push remote_name local_branch:remote_branch
```

### Send changes on all local branches to their counterparts in a given remote repository

```bash
git push --all remote_name
```

### Delete a branch in a remote repository

```bash
git push remote_name [-d|--delete] remote_branch
```

### Remove remote branches that don't have a local counterpart

```bash
git push --prune remote_name
```

### Publish tags that aren't yet in the remote repository

```bash
git push --tags
```
