# rhash

> Calculate or check common message digests. More information: <https://rhash.sourceforge.net/manpage.php>.

## Examples

### Calculate default CRC32 digests of a file

```bash
rhash path/to/file
```

### Recursively process a directory to generate an SFV file using SHA1

```bash
rhash --sha1 --recursive path/to/folder > path/to/output.sfv
```

### Verify the integrity of files based on an SFV file

```bash
rhash --check path/to/file.sfv
```

### Calculate the SHA3 digest of a text message

```bash
rhash --sha3-256 --message 'message'
```

### Calculate CRC32 digest of a file and output digest encoded in base64 using BSD format

```bash
rhash --base64 --bsd path/to/file
```

### Use custom output template

```bash
rhash --printf '%p\t%s\t%{mtime}\t%m\n' path/to/file
```
