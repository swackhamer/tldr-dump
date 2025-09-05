# ps

> Information about running processes. More information: <https://keith.github.io/xcode-man-pages/ps.1.html>.

## Examples

### List all running processes

```bash
ps aux
```

### List all running processes including the full command string

```bash
ps auxww
```

### Search for a process that matches a string

```bash
ps aux | grep string
```

### Get the parent PID of a process

```bash
ps -o ppid= -p pid
```

### Sort processes by memory usage

```bash
ps -m
```

### Sort processes by CPU usage

```bash
ps -r
```
