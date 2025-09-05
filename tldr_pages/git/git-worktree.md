# git-worktree

> Manage multiple working trees attached to the same repository. More information: <https://git-scm.com/docs/git-worktree>.

## Examples

### Create a new directory with the specified branch checked out into it

```bash
git worktree add path/to/directory branch
```

### Create a new directory with a new branch checked out into it

```bash
git worktree add path/to/directory -b new_branch
```

### List all the working directories attached to this repository

```bash
git worktree list
```

### Remove a worktree (after deleting worktree directory)

```bash
git worktree prune
```
