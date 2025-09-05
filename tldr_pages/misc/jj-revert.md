# jj-revert

> Apply the reverse of the given revision(s). More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-revert>.

## Examples

### Apply the reverse of the revisions specified by the given revsets (e.g. `B::D`, `A..D`, `B|C|D`, etc.)

```bash
jj revert [-r|--revisions] revsets
```

### Apply the reverse on top of specified revisions

```bash
jj revert [-r|--revisions] revsets [-d|--destination] revsets
```

### Apply the reverse before and/or after specified revisions

```bash
jj revert [-r|--revisions] revsets [-B|--insert-before] revsets [-A|--insert-after] revsets
```
