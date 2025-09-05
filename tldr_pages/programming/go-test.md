# go-test

> Tests Go packages (files have to end with `_test.go`). More information: <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

## Examples

### Test the package found in the current directory

```bash
go test
```

### [v]erbosely test the package in the current directory

```bash
go test -v
```

### Test the packages in the current directory and all subdirectories (note the `...`)

```bash
go test -v ./...
```

### Test the package in the current directory and run all benchmarks

```bash
go test -v -bench .
```

### Test the package in the current directory and run all benchmarks for 50 seconds

```bash
go test -v -bench . -benchtime 50s
```

### Test the package with coverage analysis

```bash
go test -cover
```
