# cupsctl

> Update or query a server's `cupsd.conf`. More information: <https://openprinting.github.io/cups/doc/man-cupsctl.html>.

## Examples

### Display the current configuration values

```bash
cupsctl
```

### Display the configuration values of a specific server

```bash
cupsctl -h server[:port]
```

### Enable encryption on the connection to the scheduler

```bash
cupsctl -E
```

### Enable or disable debug logging to the `error_log` file

```bash
cupsctl --debug-logging|--no-debug-logging
```

### Enable or disable remote administration

```bash
cupsctl --remote-admin|--no-remote-admin
```

### Parse the current debug logging state

```bash
cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'
```
