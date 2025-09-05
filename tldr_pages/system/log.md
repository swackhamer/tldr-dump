# log

> View, export, and configure logging systems. More information: <https://keith.github.io/xcode-man-pages/log.1.html>.

## Examples

### Stream live system logs

```bash
log stream
```

### Stream logs sent to `syslog` from the process with a specific PID

```bash
log stream --process process_id
```

### Show logs sent to syslog from a process with a specific name

```bash
log show --predicate "process == 'process_name'"
```

### Export all logs to disk for the past hour

```bash
sudo log collect --last 1h --output path/to/file.logarchive
```
