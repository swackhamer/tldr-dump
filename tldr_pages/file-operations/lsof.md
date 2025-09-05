# lsof

> List open files and the corresponding processes. Note: Root privileges are required to list files opened by others. More information: <https://manned.org/lsof>.

## Examples

### Find the processes that have a given file open

```bash
lsof path/to/file
```

### Find the process that opened a local internet port

```bash
lsof -i :port
```

### Only output the process ID (PID)

```bash
lsof -t path/to/file
```

### List files opened by the given user

```bash
lsof -u username
```

### List files opened by the given command or process

```bash
lsof -c process_or_command_name
```

### List files opened by a specific process, given its PID

```bash
lsof -p PID
```

### List open files in a directory

```bash
lsof +D path/to/directory
```

### Find the process that is listening on a local IPv6 TCP port and don't convert network or port numbers

```bash
lsof -i6TCP:port -sTCP:LISTEN -n -P
```
