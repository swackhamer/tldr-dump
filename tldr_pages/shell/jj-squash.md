# jj-squash

> Move changes from a revision into another revision. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-squash>.

## Examples

### Move all changes from current revision to its parent

```bash
jj squash
```

### Move all changes from given revision to its parent

```bash
jj squash [-r|--revision] revset
```

### Move all changes from given revision(s) to given other revision

```bash
jj squash [-f|--from] revsets [-t|--into] revset
```

### Interactively choose which parts to squash

```bash
jj squash [-i|--interactive]
```
