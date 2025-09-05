# sha512sum

> Calculate SHA512 cryptographic checksums. More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

## Examples

### Calculate the SHA512 checksum for one or more files

```bash
sha512sum path/to/file1 path/to/file2 ...
```

### Calculate and save the list of SHA512 checksums to a file

```bash
sha512sum path/to/file1 path/to/file2 ... > path/to/file.sha512
```

### Calculate a SHA512 checksum from `stdin`

```bash
command | sha512sum
```

### Read a file of SHA512 checksums and filenames and verify all files have matching checksums

```bash
sha512sum [-c|--check] path/to/file.sha512
```

### Only show a message for missing files or when verification fails

```bash
sha512sum [-c|--check] --quiet path/to/file.sha512
```

### Only show a message when verification fails, ignoring missing files

```bash
sha512sum --ignore-missing [-c|--check] --quiet path/to/file.sha512
```

### Check a known SHA512 checksum of a file

```bash
echo known_sha512_checksum_of_the_file path/to/file | sha512sum [-c|--check]
```
