# dunstctl

> Control the `dunst` notification daemon. More information: <https://dunst-project.org/documentation/dunstctl>.

## Examples

### Pause/Unpause/Toggle desktop notifications

```bash
dunstctl set-paused true|false|toggle
```

### Close all notifications

```bash
dunstctl close-all
```

### Delete all notifications from history

```bash
dunstctl history-clear
```

### Display the latest notification from history

```bash
dunstctl history-pop
```

### Reload the configuration file

```bash
dunstctl reload
```

### Display help

```bash
dunstctl [-h|--help]
```
