# jj-restore

> Restore files from another revision. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-restore>.

## Examples

### Restore files from a revision into another revision

```bash
jj restore [-f|--from] revset [-t|--into] revset filesets
```

### Undo the changes in a revision as compared to the merge of its parents

```bash
jj restore [-c|--changes-in] revset filesets
```

### Interactively choose what parts to restore

```bash
jj restore [-f|--from] revset [-t|--into] revset [-i|--interactive]
```
