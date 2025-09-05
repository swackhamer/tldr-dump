# md5

> Calculate MD5 cryptographic checksums. More information: <https://keith.github.io/xcode-man-pages/md5.1.html>.

## Examples

### Calculate the MD5 checksum for a file

```bash
md5 path/to/file
```

### Calculate MD5 checksums for multiple files

```bash
md5 path/to/file1 path/to/file2 ...
```

### Output only the md5 checksum (no filename)

```bash
md5 -q path/to/file
```

### Print a checksum of the given string

```bash
md5 -s "string"
```
