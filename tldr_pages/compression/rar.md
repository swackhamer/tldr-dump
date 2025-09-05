# rar

> The RAR archiver. Supports multi-volume archives that can be optionally self-extracting. More information: <https://manned.org/rar>.

## Examples

### Archive 1 or more files

```bash
rar a path/to/archive_name.rar path/to/file1 path/to/file2 path/to/file3 ...
```

### Archive a directory

```bash
rar a path/to/archive_name.rar path/to/directory
```

### Split the archive into parts of equal size (50M)

```bash
rar a -v50M -R path/to/archive_name.rar path/to/file_or_directory
```

### Password protect the resulting archive

```bash
rar a -ppassword path/to/archive_name.rar path/to/file_or_directory
```

### Encrypt file data and headers with password

```bash
rar a -hppassword path/to/archive_name.rar path/to/file_or_directory
```

### Use a specific compression level (0-5)

```bash
rar a -mcompression_level path/to/archive_name.rar path/to/file_or_directory
```
