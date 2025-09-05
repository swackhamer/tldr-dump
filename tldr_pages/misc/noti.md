# noti

> Monitor a process and trigger a banner notification. More information: <https://github.com/variadico/noti>.

## Examples

### Display a notification when tar finishes compressing files

```bash
noti tar -cjf example.tar.bz2 example/
```

### Display a notification even when you put it after the command to watch

```bash
command_to_watch; noti
```

### Monitor a process by PID and trigger a notification when the PID disappears

```bash
noti [-w|--pwatch] process_id
```
