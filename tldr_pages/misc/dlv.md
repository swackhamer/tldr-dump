# dlv

> Debugger for the Go programming language. More information: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

## Examples

### Compile and begin debugging the main package in the current directory (by default, with no arguments)

```bash
dlv debug
```

### Compile and begin debugging a specific package

```bash
dlv debug package arguments
```

### Compile a test binary and begin debugging the compiled program

```bash
dlv test
```

### Connect to a headless debug server

```bash
dlv connect ip_address
```

### Attach to a running process and begin debugging

```bash
dlv attach pid
```

### Compile and begin tracing a program

```bash
dlv trace package --regexp 'regex'
```
