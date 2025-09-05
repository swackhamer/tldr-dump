# jj-log

> Show revision history as a graph. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-log>.

## Examples

### Show revision history as a graph

```bash
jj log
```

### Show only given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.)

```bash
jj log [-r|--revisions] revsets
```

### Show log with a particular template for each line (e.g. 5 characters of commit hash and author)

```bash
jj log [-T|--template] 'commit_id.shortest(5) ++ " " ++ author'
```
