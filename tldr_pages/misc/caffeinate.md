# caffeinate

> Prevent macOS from sleeping. More information: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

## Examples

### Prevent the display from sleeping

```bash
caffeinate -d
```

### Prevent from sleeping for 1 hour (3600 seconds)

```bash
caffeinate -u -t 3600
```

### Fork a process, exec "make" in it, and prevent sleep as long as that process is running

```bash
caffeinate -i make
```

### Prevent from sleeping until a process with the specified PID completes

```bash
caffeinate -w pid
```

### Prevent disk from sleeping (use `<Ctrl c>` to exit)

```bash
caffeinate -m
```
