# jj-rebase

> Move revisions to different parent(s). More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-rebase>.

## Examples

### Move given revisions to a different parent(s)

```bash
jj rebase [-r|--revisions] revset [-d|--destination] revset
```

### Move given revisions and all their descendants

```bash
jj rebase [-s|--source] revset [-d|--destination] revset
```

### Move all revisions in the branch containing given revisions

```bash
jj rebase [-b|--branch] revset [-d|--destination] revset
```

### Move revisions to before and/or after other revisions

```bash
jj rebase [-r|--revisions] revset [-B|--insert-before] revset [-A|--insert-after] revset
```
