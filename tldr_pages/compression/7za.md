# 7za

> File archiver with a high compression ratio. Similar to `7z` except that it supports fewer file types but is cross-platform. More information: <https://manned.org/7za>.

## Examples

### [a]rchive a file or directory

```bash
7za a path/to/archive.7z path/to/file_or_directory
```

### Encrypt an existing archive (including file names)

```bash
7za a path/to/encrypted.7z -ppassword -mhe=on path/to/archive.7z
```

### E[x]tract an archive preserving the original directory structure

```bash
7za x path/to/archive.7z
```

### E[x]tract an archive to a specific directory

```bash
7za x path/to/archive.7z -opath/to/output
```

### E[x]tract an archive to `stdout`

```bash
7za x path/to/archive.7z -so
```

### [a]rchive using a specific archive type

```bash
7za a -t7z|bzip2|gzip|lzip|tar|... path/to/archive.7z path/to/file_or_directory
```

### [l]ist the contents of an archive

```bash
7za l path/to/archive.7z
```

### Set the level of compression (higher means more compression, but slower)

```bash
7za a path/to/archive.7z -mx=0|1|3|5|7|9 path/to/file_or_directory
```
