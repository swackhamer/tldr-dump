# xteddy

> A cuddly teddy bear for your X Windows desktop. More information: <https://manned.org/xteddy>.

## Examples

### Display a cuddly teddy bear on your X desktop

```bash
xteddy
```

### Use the window manager to display the teddy bear and ignore the "quit" (`q`) command

```bash
xteddy -wm -noquit
```

### Make the teddy bear stay on top of all other windows

```bash
xteddy -float
```

### Display another image [F]ile instead of the cuddly teddy bear

```bash
xteddy -F path/to/image
```

### Set the initial location of the teddy bear (`width` and `height` are ignored)

```bash
xteddy -geometry widthxheight+x+y
```
