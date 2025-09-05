# vdir

> Verbosely list directory contents. Drop-in replacement for `ls -l -b`. More information: <https://manned.org/vdir>.

## Examples

### List files and directories in the current directory, one per line, with details

```bash
vdir
```

### List with sizes displayed in human-readable units (KB, MB, GB)

```bash
vdir [-h|--human-readable]
```

### List including hidden files (starting with a dot)

```bash
vdir [-a|--all]
```

### List files and directories sorting entries by size (largest first)

```bash
vdir -S
```

### List files and directories sorting entries by modification time (newest first)

```bash
vdir -t
```

### List grouping directories first

```bash
vdir --group-directories-first
```

### Recursively list all files and directories in a specific directory

```bash
vdir [-R|--recursive] path/to/directory
```
