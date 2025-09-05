# jj-diff

> Compare file contents between two revisions. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-diff>.

## Examples

### Show changes of current revision

```bash
jj diff
```

### Show changes of given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.)

```bash
jj diff [-r|--revisions] revsets
```

### Show changes from given revision to given revision

```bash
jj diff [-f|--from] from_revset [-t|--to] to_revset
```

### Show diff statistics

```bash
jj diff --stat
```

### Show a Git-format diff

```bash
jj diff --git
```
