# bzip2

> A block-sorting file compressor. See also: `bzcat`, `bunzip2`, `bzip2recover`. More information: <https://manned.org/bzip2>.

## Examples

### Compress a file

```bash
bzip2 path/to/file_to_compress
```

### Decompress a file

```bash
bzip2 [-d|--decompress] path/to/compressed_file.bz2
```

### Decompress a file to `stdout`

```bash
bzip2 [-dc|--decompress --stdout] path/to/compressed_file.bz2
```

### Test the integrity of each file inside the archive file

```bash
bzip2 [-t|--test] path/to/compressed_file.bz2
```

### Show the compression ratio for each file processed with detailed information

```bash
bzip2 [-v|--verbose] path/to/compressed_files.bz2
```

### Decompress a file overwriting existing files

```bash
bzip2 [-f|--force] path/to/compressed_file.bz2
```

### Display help

```bash
bzip2 [-h|--help]
```
