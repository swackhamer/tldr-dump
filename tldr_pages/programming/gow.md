# gow

> Watches Go files and restarts the app on changes. More information: <https://github.com/mitranim/gow>.

## Examples

### Start and watch the current directory

```bash
gow run .
```

### Start the application with the specified arguments

```bash
gow run . argument1 argument2 ...
```

### Watch subdirectories in verbose mode

```bash
gow -v -w=path/to/directory1,path/to/directory2,... run .
```

### Watch the specified file extensions

```bash
gow -e=go,html run .
```

### Display help

```bash
gow -h
```
