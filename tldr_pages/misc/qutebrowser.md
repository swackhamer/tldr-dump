# qutebrowser

> A keyboard-driven, vim-like browser based on PyQt5. More information: <https://qutebrowser.org/doc/qutebrowser.1.html>.

## Examples

### Open qutebrowser with a specified storage directory

```bash
qutebrowser --basedir path/to/directory
```

### Open a qutebrowser instance with temporary settings

```bash
qutebrowser --set content.geolocation true|false
```

### Restore a named session of a qutebrowser instance

```bash
qutebrowser --restore session_name
```

### Launch qutebrowser, opening all URLs using the specified method

```bash
qutebrowser --target auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window
```

### Open qutebrowser with a temporary base directory and print logs to `stdout` as JSON

```bash
qutebrowser --temp-basedir --json-logging
```
