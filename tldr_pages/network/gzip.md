# gzip

> Compress/uncompress files with `gzip` compression (LZ77). More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

## Examples

### Compress a file, replacing it with a `gzip` archive

```bash
gzip path/to/file
```

### Decompress a file, replacing it with the original uncompressed version

```bash
gzip [-d|--decompress] path/to/file.gz
```

### Compress a file, keeping the original file

```bash
gzip [-k|--keep] path/to/file
```

### Compress a file, specifying the output filename

```bash
gzip [-c|--stdout] path/to/file > path/to/compressed_file.gz
```

### Decompress a `gzip` archive specifying the output filename

```bash
gzip [-c|--stdout] [-d|--decompress] path/to/file.gz > path/to/uncompressed_file
```

### Specify the compression level. 1 is the fastest (low compression), 9 is the slowest (high compression), 6 is the default

```bash
gzip -1..9 [-c|--stdout] path/to/file > path/to/compressed_file.gz
```

### Display the name and reduction percentage for each file compressed or decompressed

```bash
gzip [-v|--verbose] [-d|--decompress] path/to/file.gz
```
