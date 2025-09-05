# nkf

> Network kanji filter: convert kanji code from one encoding to another. More information: <https://manned.org/nkf>.

## Examples

### Convert to UTF-8 encoding

```bash
nkf -w path/to/file.txt
```

### Convert to SHIFT_JIS encoding

```bash
nkf -s path/to/file.txt
```

### Convert to UTF-8 encoding and overwrite the file

```bash
nkf -w --overwrite path/to/file.txt
```

### Use LF as the new line code and overwrite (UNIX type)

```bash
nkf -d --overwrite path/to/file.txt
```

### Use CRLF as the new line code and overwrite (windows type)

```bash
nkf -c --overwrite path/to/file.txt
```

### Decrypt mime file and overwrite

```bash
nkf -m --overwrite path/to/file.txt
```
