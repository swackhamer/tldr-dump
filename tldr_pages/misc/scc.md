# scc

> Count lines of code. Written in Go. More information: <https://github.com/boyter/scc>.

## Examples

### Print lines of code in the current directory

```bash
scc
```

### Print lines of code in the target directory

```bash
scc path/to/directory
```

### Display output for every file

```bash
scc --by-file
```

### Display output using a specific output format (defaults to `tabular`)

```bash
scc [-f|--format] tabular|wide|json|csv|cloc-yaml|html|html-table
```

### Only count files with specific file extensions

```bash
scc [-i|--include-ext] go,java,js
```

### Exclude directories from being counted

```bash
scc --exclude-dir .git,.hg
```

### Display output and sort by column (defaults to by files)

```bash
scc [-s|--sort] files|name|lines|blanks|code|comments|complexity
```

### Display help

```bash
scc [-h|--help]
```
