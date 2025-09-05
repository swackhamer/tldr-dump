# pake

> Turn any webpage into a desktop app with Rust/Tauri. More information: <https://github.com/tw93/Pake>.

## Examples

### Package a web page

```bash
pake https://www.google.com/
```

### Package a web page with a specific window size

```bash
pake --width 800 --height 600 https://www.google.com/
```

### Package a web page with a custom application name and icon

```bash
pake --name Google --icon path/to/icon.ico https://www.google.com/
```

### Package a web page with a non-resizable window

```bash
pake --no-resizable https://www.google.com/
```

### Package a web page with fullscreen mode

```bash
pake --fullscreen https://www.google.com/
```

### Package a web page with a transparent title bar

```bash
pake --transparent https://www.google.com/
```
