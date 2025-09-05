# cavif

> Convert PNG/JPEG images to AVIF. Written in Rust. See also: `convert`. More information: <https://github.com/kornelski/cavif-rs>.

## Examples

### Convert a JPEG file to AVIF, saving it to `file.avif`

```bash
cavif path/to/image.jpg
```

### Adjust the image quality and convert a PNG file to AVIF

```bash
cavif --quality 1..100 path/to/image.png
```

### Specify the output location

```bash
cavif path/to/image.jpg --output path/to/output.avif
```

### Overwrite the destination file if it already exists

```bash
cavif --overwrite path/to/image.jpg
```
