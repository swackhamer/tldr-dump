# git-squash

> Squash multiple commits into a single commit. Part of `git-extras`. More information: <https://manned.org/git-squash>.

## Examples

### Merge all commits from a specific branch into the current branch as a single commit

```bash
git squash source_branch
```

### Squash all commits starting with a specific commit on the current branch

```bash
git squash commit
```

### Squash the `n` latest commits and commit with a message

```bash
git squash HEAD~n "message"
```

### Squash the `n` latest commits and commit concatenating all individual messages

```bash
git squash --squash-msg HEAD~n
```
