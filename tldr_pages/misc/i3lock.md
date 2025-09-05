# i3lock

> Simple screen locker built for the i3 window manager. More information: <https://manned.org/i3lock>.

## Examples

### Lock the screen showing a white background

```bash
i3lock
```

### Lock the screen with a simple color background (rrggbb format)

```bash
i3lock [-c|--color] 0000ff
```

### Lock the screen to a PNG background

```bash
i3lock [-i|--image] path/to/file.png
```

### Lock the screen and disable the unlock indicator (removes feedback on keypress)

```bash
i3lock [-u|--no-unlock-indicator]
```

### Lock the screen and don't hide the mouse pointer

```bash
i3lock [-p|--pointer] default
```

### Lock the screen to a PNG background tiled over all monitors

```bash
i3lock [-i|--image] path/to/file.png [-t|--tiling]
```

### Lock the screen and show the number of failed login attempts

```bash
i3lock [-f|--show-failed-attempts]
```
