# xprop

> Display window and font properties in an X server. More information: <https://manned.org/xprop>.

## Examples

### Display the name of the root window

```bash
xprop -root WM_NAME
```

### Display the window manager hints for a window

```bash
xprop -name "window_name" WM_HINTS
```

### Display the point size of a font

```bash
xprop -font "font_name" POINT_SIZE
```

### Display all the properties of the window with the ID 0x200007

```bash
xprop -id 0x200007
```
