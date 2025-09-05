# git-prune

> Git command for pruning all unreachable objects from the object database. This command is often not used directly but as an internal command that is used by Git gc. More information: <https://git-scm.com/docs/git-prune>.

## Examples

### Report what would be removed by Git prune without removing it

```bash
git prune [-n|--dry-run]
```

### Prune unreachable objects and display what has been pruned to `stdout`

```bash
git prune [-v|--verbose]
```

### Prune unreachable objects while showing progress

```bash
git prune --progress
```
