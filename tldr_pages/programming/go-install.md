# go-install

> Compile and install packages named by the import paths. More information: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

## Examples

### Compile and install the current package

```bash
go install
```

### Compile and install a specific local package

```bash
go install path/to/package
```

### Install the latest version of a program, ignoring `go.mod` in the current directory

```bash
go install golang.org/x/tools/gopls@latest
```

### Install a program at the version selected by `go.mod` in the current directory

```bash
go install golang.org/x/tools/gopls
```
