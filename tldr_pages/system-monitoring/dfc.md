# dfc

> Get an overview of the filesystem disk space usage with colors and graphs. More information: <https://github.com/Rolinh/dfc>.

## Examples

### Display filesystems and their disk usage in human-readable form with colors and graphs

```bash
dfc
```

### Display all filesystems including pseudo, duplicate and inaccessible filesystems

```bash
dfc -a
```

### Display filesystems without color

```bash
dfc -c never
```

### Display filesystems containing "ext" in the filesystem type

```bash
dfc -t ext
```
