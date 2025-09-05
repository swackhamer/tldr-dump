# sha256sum

> Calculate SHA256 cryptographic checksums. More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

## Examples

### Calculate the SHA256 checksum for one or more files

```bash
sha256sum path/to/file1 path/to/file2 ...
```

### Calculate and save the list of SHA256 checksums to a file

```bash
sha256sum path/to/file1 path/to/file2 ... > path/to/file.sha256
```

### Calculate a SHA256 checksum from `stdin`

```bash
command | sha256sum
```

### Read a file of SHA256 checksums and filenames and verify all files have matching checksums

```bash
sha256sum [-c|--check] path/to/file.sha256
```

### Only show a message for missing files or when verification fails

```bash
sha256sum [-c|--check] --quiet path/to/file.sha256
```

### Only show a message when verification fails, ignoring missing files

```bash
sha256sum --ignore-missing [-c|--check] --quiet path/to/file.sha256
```

### Check a known SHA256 checksum of a file

```bash
echo known_sha256_checksum_of_the_file path/to/file | sha256sum [-c|--check]
```
