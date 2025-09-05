# pkill

> Signal process by name. Mostly used for stopping processes. More information: <https://www.manned.org/pkill>.

## Examples

### Kill all processes which match

```bash
pkill "process_name"
```

### Kill all processes which match their full command instead of just the process name

```bash
pkill [-f|--full] "command_name"
```

### Force kill matching processes (can't be blocked)

```bash
pkill -9 "process_name"
```

### Send SIGUSR1 signal to processes which match

```bash
pkill -USR1 "process_name"
```

### Kill the main `firefox` process to close the browser

```bash
pkill [-o|--oldest] "firefox"
```
