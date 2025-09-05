# tree

> Show the contents of the current directory as a tree. More information: <https://manned.org/tree>.

## Examples

### Print files and directories up to 'num' levels of depth (where 1 means the current directory)

```bash
tree -L num
```

### Print directories only

```bash
tree -d
```

### Print hidden files too with colorization on

```bash
tree -a -C
```

### Print the tree without indentation lines, showing the full path instead (use `-N` to not escape non-printable characters)

```bash
tree -i -f
```

### Print the size of each file and the cumulative size of each directory, in human-readable format

```bash
tree -s -h --du
```

### Print files within the tree hierarchy, using a wildcard (glob) pattern, and pruning out directories that don't contain matching files

```bash
tree -P '*.txt' --prune
```

### Print directories within the tree hierarchy, using the wildcard (glob) pattern, and pruning out directories that aren't ancestors of the wanted one

```bash
tree -P directory_name --matchdirs --prune
```

### Print the tree ignoring the given directories

```bash
tree -I 'directory_name1|directory_name2'
```
