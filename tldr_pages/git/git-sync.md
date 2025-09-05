# git-sync

> Sync local branches with remote branches. Part of `git-extras`. More information: <https://manned.org/git-sync>.

## Examples

### Sync the current local branch with its remote branch

```bash
git sync
```

### Sync the current local branch with the remote main branch

```bash
git sync origin main
```

### Sync without cleaning untracked files

```bash
git sync [-s|--soft] remote_name branch_name
```
