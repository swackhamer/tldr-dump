# pngquant

> PNG converter and lossy image compressor. More information: <https://manned.org/pngquant>.

## Examples

### Compress a specific PNG as much as possible and write result to a new file

```bash
pngquant path/to/file.png
```

### Compress a specific PNG and override original

```bash
pngquant --ext .png --force path/to/file.png
```

### Try to compress a specific PNG with custom quality (skip if below the min value)

```bash
pngquant --quality 0-100 path/to/file.png
```

### Compress a specific PNG with the number of colors reduced to 64

```bash
pngquant 64 path/to/file.png
```

### Compress a specific PNG and skip if the file is larger than the original

```bash
pngquant --skip-if-larger path/to/file.png
```

### Compress a specific PNG and remove metadata

```bash
pngquant --strip path/to/file.png
```

### Compress a specific PNG and save it to the given path

```bash
pngquant path/to/file.png --output path/to/file.png
```

### Compress a specific PNG and show progress

```bash
pngquant --verbose path/to/file.png
```
