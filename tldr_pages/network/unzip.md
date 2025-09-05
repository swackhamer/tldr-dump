# unzip

> Extract files/directories from Zip archives. See also: `zip`. More information: <https://manned.org/unzip>.

## Examples

### Extract all files/directories from specific archives into the current directory

```bash
unzip path/to/archive1.zip path/to/archive2.zip ...
```

### Extract files/directories from archives to a specific path

```bash
unzip path/to/archive1.zip path/to/archive2.zip ... -d path/to/output
```

### Extract files/directories from archives to `stdout` alongside the extracted file names

```bash
unzip -c path/to/archive1.zip path/to/archive2.zip ...
```

### Extract an archive created on Windows, containing files with non-ASCII (e.g. Chinese or Japanese characters) filenames

```bash
unzip -O gbk path/to/archive1.zip path/to/archive2.zip ...
```

### List the contents of a specific archive without extracting them

```bash
unzip -l path/to/archive.zip
```

### Extract a specific file from an archive

```bash
unzip -j path/to/archive.zip path/to/file1_in_archive path/to/file2_in_archive ...
```
