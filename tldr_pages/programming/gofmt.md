# gofmt

> Format Go source code. More information: <https://pkg.go.dev/cmd/gofmt>.

## Examples

### Format a file and display the result to the console

```bash
gofmt source.go
```

### Format a file, overwriting the original file in-place

```bash
gofmt -w source.go
```

### Format a file, and then simplify the code, overwriting the original file

```bash
gofmt -s -w source.go
```

### Print all (including spurious) errors

```bash
gofmt -e source.go
```
