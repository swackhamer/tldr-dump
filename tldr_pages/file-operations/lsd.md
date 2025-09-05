# lsd

> List directory contents. The next generation `ls` command, written in Rust. More information: <https://github.com/Peltoche/lsd>.

## Examples

### List files and directories, one per line

```bash
lsd [-1|--oneline]
```

### List all files and directories, including hidden ones, in the current directory

```bash
lsd [-a|--all]
```

### List files and directories with trailing `/` added to directory names

```bash
lsd [-F|--classify]
```

### List all files and directories in long format (permissions, ownership, size in human-readable format, and modification date)

```bash
lsd [-lha|--long --human-readable --all]
```

### List files and directories in long format, sorted by size (descending)

```bash
lsd [-lS|--long --sizesort]
```

### List files and directories in long format, sorted by modification date (oldest first)

```bash
lsd [-ltr|--long --timesort --reverse]
```

### Only list directories

```bash
lsd [-d|--directory-only] */
```

### Recursively list all directories in a tree format

```bash
lsd --tree [-d|--directory-only]
```
