# kitty

> A fast, feature-rich, GPU based terminal emulator. More information: <https://sw.kovidgoyal.net/kitty/>.

## Examples

### Open a new terminal

```bash
kitty
```

### Open a terminal with the specified title for the window

```bash
kitty --title "title"
```

### Start the theme-chooser builtin

```bash
kitty +kitten themes
```

### Display an image in the terminal

```bash
kitty +kitten icat path/to/image
```

### Copy the contents of `stdin` to the clipboard

```bash
echo example | kitty +kitten clipboard
```
