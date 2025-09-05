# chromium

> Open-source web browser principally developed and maintained by Google. Note: You may need to replace the `chromium` command with your desired web browser, such as `brave`, `google-chrome`, `opera`, or `vivaldi`. More information: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

## Examples

### Open a specific URL or file

```bash
chromium https://example.com|path/to/file.html
```

### Open in incognito mode

```bash
chromium --incognito example.com
```

### Open in a new window

```bash
chromium --new-window example.com
```

### Open in application mode (without toolbars, URL bar, buttons, etc.)

```bash
chromium --app=https://example.com
```

### Use a proxy server

```bash
chromium --proxy-server="socks5://hostname:66" example.com
```

### Open with a custom profile directory

```bash
chromium --user-data-dir=path/to/directory
```

### Open without CORS validation (useful to test an API)

```bash
chromium --user-data-dir=path/to/directory --disable-web-security
```

### Open with a DevTools window for each tab opened

```bash
chromium --auto-open-devtools-for-tabs
```
