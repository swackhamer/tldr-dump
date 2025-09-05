# basenc

> Encode or decode file or `stdin` using a specified encoding, to `stdout`. More information: <https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html>.

## Examples

### Encode a file with base64 encoding

```bash
basenc --base64 path/to/file
```

### Decode a file with base64 encoding

```bash
basenc [-d|--decode] --base64 path/to/file
```

### Encode from `stdin` with base32 encoding with 42 columns

```bash
command | basenc --base32 [-w|--wrap] 42
```

### Encode from `stdin` with base32 encoding

```bash
command | basenc --base32
```
