# xz

> Compress or decompress XZ and LZMA files. More information: <https://manned.org/xz>.

## Examples

### Compress a file using xz

```bash
xz path/to/file
```

### Decompress an XZ file

```bash
xz [-d|--decompress] path/to/file.xz
```

### Compress a file using lzma

```bash
xz [-F|--format] lzma path/to/file
```

### Decompress an LZMA file

```bash
xz [-d|--decompress] [-F|--format] lzma path/to/file.lzma
```

### Decompress a file and write to `stdout` (implies `--keep`)

```bash
xz [-d|--decompress] [-c|--stdout] path/to/file.xz
```

### Compress a file, but don't delete the original

```bash
xz [-k|--keep] path/to/file
```

### Compress a file using the fastest compression

```bash
xz -0 path/to/file
```

### Compress a file using the best compression

```bash
xz -9 path/to/file
```
