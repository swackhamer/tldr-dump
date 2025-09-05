# go

> Manage Go source code. Some subcommands such as `build` have their own usage documentation. More information: <https://pkg.go.dev/cmd/go>.

## Examples

### Download and install a package, specified by its import path

```bash
go get package_path
```

### Compile and run a source file (it has to contain a `main` package)

```bash
go run file.go
```

### Compile a source file into a named executable

```bash
go build -o executable file.go
```

### Compile the package present in the current directory

```bash
go build
```

### Execute all test cases of the current package (files have to end with `_test.go`)

```bash
go test
```

### Compile and install the current package

```bash
go install
```

### Initialize a new module in the current directory

```bash
go mod init module_name
```
