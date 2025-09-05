# hledger-web

> A web interface and API for `hledger`, a robust, friendly plain text accounting app. More information: <https://hledger.org/hledger-web.html>.

## Examples

### Start the web app, and a browser if possible, for local viewing and adding only

```bash
hledger-web
```

### As above but with a specified file, and allow editing of existing data

```bash
hledger-web [-f|--file] path/to/file.journal --allow edit
```

### Start just the web app, and accept incoming connections to the specified host and port

```bash
hledger-web --serve --host my.host.name --port 8000
```

### Start just the web app's JSON API, and allow only read access

```bash
hledger-web --serve-api --host my.host.name --allow view
```

### Show amounts converted to current market value in your base currency when known

```bash
hledger-web --value now --infer-market-prices
```

### Show the manual in Info format if possible

```bash
hledger-web --info
```

### Display help

```bash
hledger-web [-h|--help]
```
