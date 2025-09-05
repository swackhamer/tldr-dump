# go-fmt

> Format Go source files, printing the changed filenames. More information: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

## Examples

### Format Go source files in the current directory

```bash
go fmt
```

### Format a specific Go package in your import path (`$GOPATH/src`)

```bash
go fmt path/to/package
```

### Format the package in the current directory and all subdirectories (note the `...`)

```bash
go fmt ./...
```

### Print what format commands would've been run, without modifying anything

```bash
go fmt -n
```

### Print which format commands are run as they are run

```bash
go fmt -x
```
