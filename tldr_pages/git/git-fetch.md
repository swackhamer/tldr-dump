# git-fetch

> Download objects and refs from a remote repository. More information: <https://git-scm.com/docs/git-fetch>.

## Examples

### Fetch the latest changes from the default remote upstream repository (if set)

```bash
git fetch
```

### Fetch new branches from a specific remote upstream repository

```bash
git fetch remote_name
```

### Fetch the latest changes from all remote upstream repositories

```bash
git fetch --all
```

### Also fetch tags from the remote upstream repository

```bash
git fetch [-t|--tags]
```

### Delete local references to remote branches that have been deleted upstream

```bash
git fetch [-p|--prune]
```
