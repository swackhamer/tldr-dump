# jj-split

> Split a revision in two. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-split>.

## Examples

### Split the given revision into two interactively, putting the second revision on top of it

```bash
jj split [-r|--revision] revision
```

### Split out matching files from the given revision

```bash
jj split [-r|--revision] revision fileset
```

### Split the given revision, putting the second revision on top of given destination(s)

```bash
jj split [-r|--revision] revision [-d|--destination] revset
```

### Split the given revision, putting the second revision before and/or after other revision(s)

```bash
jj split [-r|--revision] revision [-B|--insert-before] revset [-A|--insert-after] revset
```

### Split the given revision into two parallel revisions

```bash
jj split [-r|--revision] revision [-p|--parallel]
```
