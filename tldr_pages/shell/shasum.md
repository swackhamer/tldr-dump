# shasum

> Calculate SHA cryptographic checksums. More information: <https://manned.org/shasum>.

## Examples

### Calculate the SHA1 checksum for one or more files

```bash
shasum path/to/file1 path/to/file2 ...
```

### Calculate the SHA checksum for one or more files with the specified algorithm

```bash
shasum --algorithm 1|224|256|384|512|512224|512256 path/to/file1 path/to/file2 ...
```

### Calculate a SHA1 checksum from `stdin`

```bash
command | shasum
```

### Calculate and save the list of SHA256 checksums to a file

```bash
shasum --algorithm 256 path/to/file1 path/to/file2 ... > path/to/file.sha256
```

### Read a file of SHA checksums and filenames and verify all files have matching checksums (the algorithm will be automatically detected)

```bash
shasum [-c|--check] path/to/file
```

### Only show a message for missing files or when verification fails

```bash
shasum [-c|--check] --quiet path/to/file
```

### Only show a message when verification fails, ignoring missing files

```bash
shasum --ignore-missing [-c|--check] --quiet path/to/file
```

### Check a known SHA checksum of a file

```bash
echo known_sha_checksum_of_the_file path/to/file | shasum [-c|--check]
```
