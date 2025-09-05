# cwebp

> Compress an image file to a WebP file. More information: <https://developers.google.com/speed/webp/docs/cwebp>.

## Examples

### Compress a WebP file with default settings (q = 75) to the [o]utput file

```bash
cwebp path/to/image_file -o path/to/output.webp
```

### Compress a WebP file with the best [q]uality and largest file size

```bash
cwebp path/to/image_file -o path/to/output.webp -q 100
```

### Compress a WebP file with the worst [q]uality and smallest file size

```bash
cwebp path/to/image_file -o path/to/output.webp -q 0
```

### Compress a WebP file and apply resize to image

```bash
cwebp path/to/image_file -o path/to/output.webp -resize width height
```

### Compress a WebP file and drop alpha channel information

```bash
cwebp path/to/image_file -o path/to/output.webp -noalpha
```
