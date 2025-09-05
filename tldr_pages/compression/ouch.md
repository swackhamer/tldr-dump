# ouch

> Utility for compressing and decompressing files and directories. More information: <https://crates.io/crates/ouch>.

## Examples

### Decompress a specific file

```bash
ouch decompress path/to/archive.tar.xz
```

### Decompress a file to a specific location

```bash
ouch decompress path/to/archive.tar.xz --dir path/to/directory
```

### Decompress multiple files

```bash
ouch decompress path/to/archive1.tar path/to/archive2.tar.gz ...
```

### Compress files

```bash
ouch compress path/to/file1 path/to/file2 ... path/to/archive.zip
```
