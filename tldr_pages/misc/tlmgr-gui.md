# tlmgr-gui

> Start a graphical user interface for `tlmgr`. `tlmgr gui` depends on the package `perl-tk`, which has to be installed manually. More information: <https://www.tug.org/texlive/doc/tlmgr.html#gui>.

## Examples

### Start a GUI for `tlmgr`

```bash
sudo tlmgr gui
```

### Start a GUI specifying the background color

```bash
sudo tlmgr gui -background "#f39bc3"
```

### Start a GUI specifying the foreground color

```bash
sudo tlmgr gui -foreground "#0ef3bd"
```

### Start a GUI specifying the font and font size

```bash
sudo tlmgr gui -font "helvetica 18"
```

### Start a GUI setting a specific geometry

```bash
sudo tlmgr gui -geometry widthxheight-xpos+ypos
```

### Start a GUI passing an arbitrary X resource string

```bash
sudo tlmgr gui -xrm xresource
```
