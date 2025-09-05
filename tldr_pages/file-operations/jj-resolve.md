# jj-resolve

> Resolve conflicted files with an external merge tool. More information: <https://jj-vcs.github.io/jj/latest/cli-reference/#jj-resolve>.

## Examples

### Resolve all conflicts

```bash
jj resolve
```

### List all conflicts

```bash
jj resolve [-l|--list]
```

### Resolve conflicts in a given revision

```bash
jj resolve [-r|--revision] revset
```

### Resolve conflicts in given files

```bash
jj resolve file1 file2 ...
```

### Resolve accepting the incoming versions

```bash
jj resolve --tool :theirs
```

### Resolve accepting the outgoing versions

```bash
jj resolve --tool :ours
```
