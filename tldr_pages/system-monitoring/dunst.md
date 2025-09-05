# dunst

> A lightweight and customizable notification daemon for X11 and Wayland. If not started manually, D-Bus will automatically start `dunst` when a notification is sent. More information: <https://dunst-project.org/documentation/dunst>.

## Examples

### Start `dunst`

```bash
dunst
```

### Display a notification on startup

```bash
dunst -startup_notification
```

### Print coming notifications to `stdout`

```bash
dunst -print
```

### Use the specified configuration file (default: `$XDG_CONFIG_HOME/dunst/dunstrc`)

```bash
dunst -config path/to/file
```
