# pbzip2

> A parallel implementation of the `bzip2` file compressor. See also: `bzip2`, `tar`. More information: <https://manned.org/pbzip2>.

## Examples

### Compress a file

```bash
pbzip2 path/to/file
```

### Compress a file using the specified number of processors

```bash
pbzip2 -p4 path/to/file
```

### Decompress a file

```bash
pbzip2 [-d|--decompress] path/to/compressed_file.bz2
```

### Display help

```bash
pbzip2 [-h|--help]
```
