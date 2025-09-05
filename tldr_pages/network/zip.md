# zip

> Package and compress (archive) files into a Zip archive. See also: `unzip`. More information: <https://manned.org/zip>.

## Examples

### Add files/directories to a specific archive

```bash
zip [-r|--recurse-paths] path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Remove files/directories from a specific archive

```bash
zip [-d|--delete] path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Archive files/directories excluding specified ones

```bash
zip [-r|--recurse-paths] path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ... [-x|--exclude] path/to/excluded_files_or_directories
```

### Archive files/directories with a specific compression level (`0` - the lowest, `9` - the highest)

```bash
zip [-r|--recurse-paths] -0..9 path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Create an encrypted archive with a specific password

```bash
zip [-re|--recurse-paths --encrypt] path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Archive files/directories to a multi-part split Zip archive (e.g. 3 GB parts)

```bash
zip [-rs|--recurse-paths --split-size] 3g path/to/compressed.zip path/to/file_or_directory1 path/to/file_or_directory2 ...
```

### Print a specific archive contents

```bash
zip [-sf|--split-size --freshen] path/to/compressed.zip
```
