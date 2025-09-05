# zstd

> Compress or decompress files with Zstandard compression. More information: <https://github.com/facebook/zstd>.

## Examples

### Compress a file into a new file with the `.zst` suffix

```bash
zstd path/to/file
```

### Decompress a file

```bash
zstd --decompress path/to/file.zst
```

### Decompress to `stdout`

```bash
zstd --decompress --stdout path/to/file.zst
```

### Compress a file specifying the compression level, where 1=fastest, 19=slowest and 3=default

```bash
zstd -level path/to/file
```

### Unlock higher compression levels (up to 22) using more memory (both for compression and decompression)

```bash
zstd --ultra -level path/to/file
```
