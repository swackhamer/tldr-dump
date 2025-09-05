# chflags

> Change file or directory flags. More information: <https://keith.github.io/xcode-man-pages/chflags.1.html>.

## Examples

### Set the `hidden` flag for a file

```bash
chflags hidden path/to/file
```

### Unset the `hidden` flag for a file

```bash
chflags nohidden path/to/file
```

### Recursively set the `uchg` flag for a directory

```bash
chflags -R uchg path/to/directory
```

### Recursively unset the `uchg` flag for a directory

```bash
chflags -R nouchg path/to/directory
```
