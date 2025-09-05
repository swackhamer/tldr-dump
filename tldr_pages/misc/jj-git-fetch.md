# jj-git-fetch

> Fetch from a Git remote, downloading objects and refs from the remote repository. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git-fetch>.

## Examples

### Fetch the latest changes from the default remote repository

```bash
jj git fetch
```

### Fetch the latest changes from a given remote repository

```bash
jj git fetch --remote remote
```

### Fetch the latest changes only from given branches

```bash
jj git fetch [-b|--branch] branch
```

### Fetch the latest changes from all remotes

```bash
jj git fetch --all-remote
```
