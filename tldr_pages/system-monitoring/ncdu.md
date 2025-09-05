# ncdu

> Disk usage analyzer with an ncurses interface. More information: <https://manned.org/ncdu>.

## Examples

### Analyze the current working directory

```bash
ncdu
```

### Colorize output

```bash
ncdu --color dark|off
```

### Analyze a given directory

```bash
ncdu path/to/directory
```

### Save results to a file

```bash
ncdu -o path/to/file
```

### Exclude files that match a pattern, argument can be given multiple times to add more patterns

```bash
ncdu --exclude '*.txt'
```
