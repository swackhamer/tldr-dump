# notifyd

> Notification server. It should not be invoked manually. More information: <https://keith.github.io/xcode-man-pages/notifyd.8.html>.

## Examples

### Start the daemon

```bash
notifyd
```

### Log debug messages to the default log file (`/var/log/notifyd.log`)

```bash
notifyd -d
```

### Log debug messages to an alternate log file

```bash
notifyd -d -log_file path/to/log_file
```
