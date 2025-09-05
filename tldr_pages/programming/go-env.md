# go-env

> Manage environment variables used by the Go toolchain. More information: <https://pkg.go.dev/cmd/go#hdr-Print_Go_environment_information>.

## Examples

### Show all environment variables

```bash
go env
```

### Show a specific environment variable

```bash
go env GOPATH
```

### Set an environment variable to a value

```bash
go env -w GOBIN=path/to/directory
```

### Reset an environment variable's value

```bash
go env -u GOBIN
```
