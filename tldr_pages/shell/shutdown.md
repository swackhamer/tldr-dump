# shutdown

> Shutdown and reboot the system. More information: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

## Examples

### Power off (halt) immediately

```bash
shutdown -h now
```

### Sleep immediately

```bash
shutdown -s now
```

### Reboot immediately

```bash
shutdown -r now
```

### Reboot in 5 minutes

```bash
shutdown -r "+5"
```

### Power off (halt) at 1:00 pm (Uses 24h clock)

```bash
shutdown -h 1300
```

### Reboot on May 10th 2042 at 11:30 am (Input format: YYMMDDHHMM)

```bash
shutdown -r 4205101130
```
