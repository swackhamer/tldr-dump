# go-tool

> Run a Go tool or command. Execute a Go command as a stand-alone binary, typically for debugging. More information: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

## Examples

### List available tools

```bash
go tool
```

### Run the go link tool

```bash
go tool link path/to/main.o
```

### Print the command that would be executed, but do not execute it (similar to `whereis`)

```bash
go tool -n command arguments
```

### View documentation for a specified tool

```bash
go tool command --help
```

### List all available cross-compilation targets

```bash
go tool dist list
```
