# git-feature

> Create or merge feature branches. Feature branches obey the format feature/name. More information: <https://manned.org/git-feature>.

## Examples

### Create and switch to a new feature branch

```bash
git feature feature_branch
```

### Merge a feature branch into the current branch creating a merge commit

```bash
git feature finish feature_branch
```

### Merge a feature branch into the current branch squashing the changes into one commit

```bash
git feature finish --squash feature_branch
```

### Send changes from a specific feature branch to its remote counterpart

```bash
git feature feature_branch [-r|--remote] remote_name
```
