# web-ext

> Manage web extension development. More information: <https://github.com/mozilla/web-ext>.

## Examples

### Run the web extension in the current directory in Firefox

```bash
web-ext run
```

### Run a web extension from a specific directory in Firefox

```bash
web-ext run --source-dir path/to/directory
```

### Display verbose execution output

```bash
web-ext run --verbose
```

### Run a web extension in Firefox Android

```bash
web-ext run --target firefox-android
```

### Lint the manifest and source files for errors

```bash
web-ext lint
```

### Build and package the extension

```bash
web-ext build
```

### Display verbose build output

```bash
web-ext build --verbose
```

### Sign a package for self-hosting

```bash
web-ext sign --api-key api_key --api-secret api_secret
```
