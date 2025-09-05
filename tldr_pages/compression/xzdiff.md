# xzdiff

> Invokes `diff` on files compressed with `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, or `zstd`. All options specified are passed directly to `diff`. More information: <https://manned.org/xzdiff>.

## Examples

### Compare two files

```bash
xzdiff path/to/file1 path/to/file2
```

### Compare two files, showing the differences side by side

```bash
xzdiff --side-by-side path/to/file1 path/to/file2
```

### Compare two files and report only that they differ (no details on what is different)

```bash
xzdiff --brief path/to/file1 path/to/file2
```

### Compare two files and report when the files are the same

```bash
xzdiff --report-identical-files path/to/file1 path/to/file2
```

### Compare two files using paginated results

```bash
xzdiff --paginate path/to/file1 path/to/file2
```
