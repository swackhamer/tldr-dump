# zcat

> Print data from `gzip` compressed files to `stdout`. More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

## Examples

### Print the uncompressed contents of a `gzip` archive to `stdout`

```bash
zcat path/to/file.txt.gz
```

### Print compression details of a `gzip` archive to `stdout`

```bash
zcat [-l|--list] path/to/file.txt.gz
```

### Test the integrity of a compressed file verbosely

```bash
zcat [-v|--verbose] [-t|--test] path/to/file.txt.gz
```

### Suppress all warnings when decompressing a file

```bash
zcat [-q|--quiet] path/to/file.txt.gz
```

### Avoid any system crashes when decompressing a file (slower output)

```bash
zcat --synchronous path/to/file.txt.gz
```
