# sha224sum

> Calculate SHA224 cryptographic checksums. More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

## Examples

### Calculate the SHA224 checksum for one or more files

```bash
sha224sum path/to/file1 path/to/file2 ...
```

### Calculate and save the list of SHA224 checksums to a file

```bash
sha224sum path/to/file1 path/to/file2 ... > path/to/file.sha224
```

### Calculate a SHA224 checksum from `stdin`

```bash
command | sha224sum
```

### Read a file of SHA224 checksums and filenames and verify all files have matching checksums

```bash
sha224sum [-c|--check] path/to/file.sha224
```

### Only show a message for missing files or when verification fails

```bash
sha224sum [-c|--check] --quiet path/to/file.sha224
```

### Only show a message when verification fails, ignoring missing files

```bash
sha224sum --ignore-missing [-c|--check] --quiet path/to/file.sha224
```

### Check a known SHA224 checksum of a file

```bash
echo known_sha224_checksum_of_the_file path/to/file | sha224sum [-c|--check]
```
