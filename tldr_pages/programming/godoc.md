# godoc

> View documentation for go packages. More information: <https://pkg.go.dev/golang.org/x/tools/cmd/godoc>.

## Examples

### Display help for a specific package

```bash
godoc fmt
```

### Display help for the function "Printf" of "fmt" package

```bash
godoc fmt Printf
```

### Serve documentation as a web server on port 6060

```bash
godoc -http=:6060
```

### Create an index file

```bash
godoc -write_index -index_files=path/to/file
```

### Use the given index file to search the docs

```bash
godoc -http=:6060 -index -index_files=path/to/file
```
