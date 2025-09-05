# microsoft-edge

> Modern web browser developed by Microsoft based on the Chromium web browser developed by Google. This command is available instead as `msedge` for Windows. Note: Additional command arguments from `chromium` may also be usable to control Microsoft Edge. More information: <https://microsoft.com/edge>.

## Examples

### Open a specific URL or file

```bash
microsoft-edge https://example.com|path/to/file.html
```

### Open in InPrivate mode

```bash
microsoft-edge --inprivate example.com
```

### Open in a new window

```bash
microsoft-edge --new-window example.com
```

### Open in application mode (without toolbars, URL bar, buttons, etc.)

```bash
microsoft-edge --app=https://example.com
```

### Use a proxy server

```bash
microsoft-edge --proxy-server="socks5://hostname:66" example.com
```

### Open with a custom profile directory

```bash
microsoft-edge --user-data-dir=path/to/directory
```

### Open without CORS validation (useful to test an API)

```bash
microsoft-edge --user-data-dir=path/to/directory --disable-web-security
```

### Open with a DevTools window for each tab opened

```bash
microsoft-edge --auto-open-devtools-for-tabs
```
