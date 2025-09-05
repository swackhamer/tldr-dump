# ntpctl

> Display information about the running instance of OpenNTPD. More information: <https://man.openbsd.org/ntpctl>.

## Examples

### Show all data

```bash
ntpctl -s [a|all]
```

### Show information about each peer

```bash
ntpctl -s [p|peers]
```

### Show the status of peers and sensors, and whether the system clock is synced

```bash
ntpctl -s [s|status]
```

### Show information about each sensor

```bash
ntpctl -s [S|Sensors]
```
