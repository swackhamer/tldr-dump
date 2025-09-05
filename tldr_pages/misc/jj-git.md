# jj-git

> Run Git-related commands for a `jj` repository. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-git>.

## Examples

### Create a new Git backed repository

```bash
jj git init
```

### Create a new repository backed by a clone of a Git repository

```bash
jj git clone source
```

### Fetch from a Git remote

```bash
jj git fetch
```

### Push all tracked bookmarks to Git remote

```bash
jj git push
```

### Push given bookmark to Git remote

```bash
jj git push [-b|--bookmark] bookmark
```
