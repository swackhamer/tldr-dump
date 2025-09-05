# gunzip

> Extract files from a `gzip` (`.gz`) archive. More information: <https://manned.org/gunzip>.

## Examples

### Extract a file from an archive, replacing the original file if it exists

```bash
gunzip archive.tar.gz
```

### Extract a file to a target destination

```bash
gunzip [-c|--stdout] archive.tar.gz > archive.tar
```

### Extract a file and keep the archive file

```bash
gunzip [-k|--keep] archive.tar.gz
```

### List the contents of a compressed file

```bash
gunzip [-l|--list] file.txt.gz
```

### Decompress an archive from `stdin`

```bash
cat path/to/archive.gz | gunzip
```
