# zdiff

> Invoke `diff` on `gzip` archives. More information: <https://manned.org/zdiff>.

## Examples

### Compare two files, uncompressing them if necessary

```bash
zdiff path/to/file1.gz path/to/file2.gz
```

### Compare a file to a `gzip` archive with the same name

```bash
zdiff path/to/file
```
