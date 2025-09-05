# zcmp

> Compare compressed files. More information: <https://manned.org/zcmp>.

## Examples

### Invoke `cmp` on two files compressed via `gzip`

```bash
zcmp path/to/file1.gz path/to/file2.gz
```

### Compare a file to its gzipped version (assuming `.gz` exists already)

```bash
zcmp path/to/file
```
