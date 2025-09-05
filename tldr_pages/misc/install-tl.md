# install-tl

> TeX Live cross-platform installer. More information: <https://tug.org/texlive/>.

## Examples

### Start the text-based installer (default on Unix systems)

```bash
install-tl -no-gui
```

### Start the GUI installer (default on macOS and Windows, requires Tcl/Tk)

```bash
install-tl -gui
```

### Install TeX Live as defined in a specific profile file

```bash
install-tl -profile path/to/texlive.profile
```

### Start the installer with the settings from a specific profile file

```bash
install-tl -init-from-file path/to/texlive.profile
```

### Start the installer for installation on a portable device, like a USB stick

```bash
install-tl -portable
```

### Display help

```bash
install-tl -help
```
