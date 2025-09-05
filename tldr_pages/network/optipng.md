# optipng

> PNG file optimization utility. More information: <https://optipng.sourceforge.net>.

## Examples

### Compress a PNG with default settings

```bash
optipng path/to/file.png
```

### Compress a PNG with the best compression

```bash
optipng -o 7 path/to/file.png
```

### Compress a PNG with the fastest compression

```bash
optipng -o 0 path/to/file.png
```

### Compress a PNG and add interlacing

```bash
optipng -i 1 path/to/file.png
```

### Compress a PNG and preserve all metadata (including file timestamps)

```bash
optipng -preserve path/to/file.png
```

### Compress a PNG and remove all metadata

```bash
optipng -strip all path/to/file.png
```
