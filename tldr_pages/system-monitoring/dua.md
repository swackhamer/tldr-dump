# dua

> Dua (Disk Usage Analyzer): get the disk space usage of a directory. More information: <https://github.com/Byron/dua-cli>.

## Examples

### Analyze specific directory

```bash
dua path/to/directory
```

### Display apparent size instead of disk usage

```bash
dua --apparent-size
```

### Count hard-linked files each time they are seen

```bash
dua --count-hard-links
```

### Aggregate the consumed space of one or more directories or files

```bash
dua aggregate
```

### Launch the terminal user interface

```bash
dua interactive
```

### Format printing byte counts

```bash
dua --format metric|binary|bytes|GB|GiB|MB|MiB
```

### Use a specific number of threads (defaults to the process number of threads)

```bash
dua --threads count
```
