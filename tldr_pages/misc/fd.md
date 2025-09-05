# fd

> An alternative to `find`. Aims to be faster and easier to use than `find`. More information: <https://github.com/sharkdp/fd#how-to-use>.

## Examples

### Recursively find files matching a specific pattern in the current directory

```bash
fd "string|regex"
```

### Find files that begin with a specific string

```bash
fd "^string"
```

### Find files with a specific extension

```bash
fd [-e|--extension] txt
```

### Find files in a specific directory

```bash
fd "string|regex" path/to/directory
```

### Include ignored and hidden files in the search

```bash
fd [-H|--hidden] [-I|--no-ignore] "string|regex"
```

### Execute a command on each search result returned

```bash
fd "string|regex" [-x|--exec] command
```
