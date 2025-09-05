# jj-evolog

> Show how a change has evolved over time, listing the previous commits it has pointed to. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-evolog>.

## Examples

### Show how a revision has evolved over time

```bash
jj evolog [-r|--revisions] revsets
```

### Show diff statistics in the evolution log

```bash
jj evolog [-r|--revisions] revsets --stat
```

### Show summary of each change in the evolution log

```bash
jj evolog [-r|--revisions] revsets [-s|--summary]
```
