# brotli

> Compress/uncompress files with Brotli compression. More information: <https://manned.org/brotli>.

## Examples

### Compress a file, creating a compressed version next to the file

```bash
brotli path/to/file
```

### Decompress a file, creating an uncompressed version next to the file

```bash
brotli [-d|--decompress] path/to/file.br
```

### Compress a file specifying the output filename

```bash
brotli path/to/file [-o|--output] path/to/compressed_output_file.br
```

### Decompress a Brotli file specifying the output filename

```bash
brotli [-d|--decompress] path/to/compressed_file.br [-o|--output] path/to/output_file
```

### Specify the compression quality (1=fastest (worst), 11=slowest (best))

```bash
brotli [-q|--quality] 11 path/to/file [-o|--output] path/to/compressed_output_file.br
```
