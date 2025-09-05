# picom-trans

> Set the window opacity for the `picom` window compositor. More information: <https://github.com/yshui/picom>.

## Examples

### Set the currently focused window opacity to a specific percentage

```bash
picom-trans --current --opacity 90
```

### Set the opacity of a window with a specific name

```bash
picom-trans --name Firefox --opacity 90
```

### Set the opacity of a specific window selected via mouse cursor

```bash
picom-trans --select --opacity 90
```

### Toggle the opacity of a specific window

```bash
picom-trans --name Firefox --toggle
```
