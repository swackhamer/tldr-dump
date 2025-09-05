# go-vet

> Check Go source code and report suspicious constructs (e.g. lint your Go source files). Go vet returns a non-zero exit code if problems are found; returns a zero exit code if no problems are found. More information: <https://pkg.go.dev/cmd/vet>.

## Examples

### Check the Go package in the current directory

```bash
go vet
```

### Check the Go package in the specified path

```bash
go vet path/to/file_or_directory
```

### List available checks that can be run with go vet

```bash
go tool vet help
```

### View details and flags for a particular check

```bash
go tool vet help check_name
```

### Display offending lines plus `n` lines of surrounding context

```bash
go vet -c=n
```

### Output analysis and errors in JSON format

```bash
go vet -json
```
