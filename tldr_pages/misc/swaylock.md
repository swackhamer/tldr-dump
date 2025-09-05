# swaylock

> Screen locking utility for Wayland compositors. More information: <https://manned.org/swaylock>.

## Examples

### Lock the screen using the config in `$HOME/.swaylock/config` or `$XDG_CONFIG_HOME/swaylock/config`

```bash
swaylock
```

### Lock the screen with a simple color background (`rrggbb` format)

```bash
swaylock [-c|--color] 0000ff
```

### Lock the screen with a background image

```bash
swaylock [-i|--image] path/to/image
```

### Lock the screen and disable the unlock indicator (removes feedback on keypress)

```bash
swaylock [-u|--no-unlock-indicator]
```

### Detach from the controlling terminal after locking (like `i3lock`)

```bash
swaylock [-f|--daemonize]
```

### Lock the screen with a background image tiled over all monitors

```bash
swaylock [-i|--image] path/to/image [-t|--tiling]
```

### Lock the screen and show the number of failed login attempts

```bash
swaylock [-F|--show-failed-attempts]
```

### Load the configuration from a specific file

```bash
swaylock [-C|--config] path/to/config
```
