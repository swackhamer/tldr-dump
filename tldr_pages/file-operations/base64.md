# base64

> Encode or decode file or `stdin` to/from base64, to `stdout` or another file. More information: <https://keith.github.io/xcode-man-pages/bintrans.1>.

## Examples

### Encode a file to `stdout`

```bash
base64 [-i|--input] path/to/file
```

### Encode a file to the specified output file

```bash
base64 [-i|--input] path/to/input_file [-o|--output] path/to/output_file
```

### Wrap encoded output at a specific width (`0` disables wrapping)

```bash
base64 [-b|--break] 0|76|... path/to/file
```

### Decode a file to `stdout`

```bash
base64 [-d|--decode] [-i|--input] path/to/file
```

### Encode from `stdin` to `stdout`

```bash
command | base64
```

### Decode from `stdin` to `stdout`

```bash
command | base64 [-d|--decode]
```
