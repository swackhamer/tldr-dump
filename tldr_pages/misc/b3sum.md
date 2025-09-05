# b3sum

> Calculate BLAKE3 cryptographic checksums. More information: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

## Examples

### Calculate the BLAKE3 checksum for one or more files

```bash
b3sum path/to/file1 path/to/file2 ...
```

### Calculate and save the list of BLAKE3 checksums to a file

```bash
b3sum path/to/file1 path/to/file2 ... > path/to/file.b3
```

### Calculate a BLAKE3 checksum from `stdin`

```bash
command | b3sum
```

### Read a file of BLAKE3 checksums and filenames and verify all files have matching checksums

```bash
b3sum [-c|--check] path/to/file.b3
```

### Only show a message for missing files or when verification fails

```bash
b3sum [-c|--check] --quiet path/to/file.b3
```

### Check a known BLAKE3 checksum of a file

```bash
echo known_blake3_checksum_of_the_file path/to/file | b3sum [-c|--check]
```
