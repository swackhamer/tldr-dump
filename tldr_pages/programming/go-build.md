# go-build

> Compile Go sources. More information: <https://pkg.go.dev/cmd/go#hdr-Compile_packages_and_dependencies>.

## Examples

### Compile a 'package main' file (output will be the filename without extension)

```bash
go build path/to/main.go
```

### Compile, specifying the output filename

```bash
go build -o path/to/binary path/to/source.go
```

### Compile a package

```bash
go build -o path/to/binary path/to/package
```

### Compile a main package into an executable, enabling data race detection

```bash
go build -race -o path/to/executable path/to/main/package
```
