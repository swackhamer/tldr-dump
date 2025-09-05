# reflex

> Watch a directory and rerun a command when certain files change. More information: <https://github.com/cespare/reflex>.

## Examples

### Rebuild with `make` if any file changes

```bash
reflex make
```

### Compile and run Go application if any `.go` file changes

```bash
reflex --regex='\.go$' go run .
```

### Ignore a directory when watching for changes

```bash
reflex --inverse-regex='^dir/' command
```

### Run command when reflex starts and restarts on file changes

```bash
reflex --start-service=true command
```

### Substitute the filename that changed in

```bash
reflex -- echo {}
```
