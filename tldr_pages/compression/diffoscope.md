# diffoscope

> Compare files, archives, and directories. More information: <https://diffoscope.org>.

## Examples

### Compare two files

```bash
diffoscope path/to/file1 path/to/file2
```

### Compare two files without displaying a progress bar

```bash
diffoscope --no-progress path/to/file1 path/to/file2
```

### Compare two files and write an HTML-report to a file (use `-` for `stdout`)

```bash
diffoscope --html path/to/outfile|- path/to/file1 path/to/file2
```

### Compare two directories excluding files with a name matching a specified pattern

```bash
diffoscope --exclude pattern path/to/directory1 path/to/directory2
```

### Compare two directories and control whether directory metadata is considered

```bash
diffoscope --exclude-directory-metadata auto|yes|no|recursive path/to/directory1 path/to/directory2
```
