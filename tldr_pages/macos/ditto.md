# ditto

> Copy files and directories. More information: <https://keith.github.io/xcode-man-pages/ditto.1.html>.

## Examples

### Overwrite contents of destination directory with contents of source directory

```bash
ditto path/to/source_directory path/to/destination_directory
```

### Print a line to the Terminal window for every file that's being copied

```bash
ditto -V path/to/source_directory path/to/destination_directory
```

### Copy a given file or directory, while retaining the original file permissions

```bash
ditto -rsrc path/to/source_directory path/to/destination_directory
```
