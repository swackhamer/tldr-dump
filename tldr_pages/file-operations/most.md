# most

> Open one or several files for interactive reading, allowing scrolling and search. More information: <https://manned.org/most>.

## Examples

### Open a file

```bash
most path/to/file
```

### Open several files

```bash
most path/to/file1 path/to/file2 ...
```

### Open a file at the first occurrence of "string"

```bash
most path/to/file +/string
```

### Move through opened files

```bash
<:><n><ArrowUp>|<ArrowDown>
```

### Jump to the 100th line

```bash
<j>100<Enter>
```

### Edit current file

```bash
<e>
```

### Split the current window in half

```bash
<CTRL x><o>
```

### Exit

```bash
<q>
```
