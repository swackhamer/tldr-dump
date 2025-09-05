# sha1sum

> Calculate SHA1 cryptographic checksums. More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha1sum-invocation.html>.

## Examples

### Calculate the SHA1 checksum for one or more files

```bash
sha1sum path/to/file1 path/to/file2 ...
```

### Calculate and save the list of SHA1 checksums to a file

```bash
sha1sum path/to/file1 path/to/file2 ... > path/to/file.sha1
```

### Calculate a SHA1 checksum from `stdin`

```bash
command | sha1sum
```

### Read a file of SHA1 checksums and filenames and verify all files have matching checksums

```bash
sha1sum [-c|--check] path/to/file.sha1
```

### Only show a message for missing files or when verification fails

```bash
sha1sum [-c|--check] --quiet path/to/file.sha1
```

### Only show a message when verification fails, ignoring missing files

```bash
sha1sum --ignore-missing [-c|--check] --quiet path/to/file.sha1
```

### Check a known SHA1 checksum of a file

```bash
echo known_sha1_checksum_of_the_file path/to/file | sha1sum [-c|--check]
```
