# mktemp

> Create a temporary file or directory. More information: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

## Examples

### Create an empty temporary file and print its absolute path

```bash
mktemp
```

### Use a custom directory (defaults to the output of `getconf DARWIN_USER_TEMP_DIR`, or `/tmp`)

```bash
mktemp --tmpdir /path/to/tempdir
```

### Use a custom path template (`X`s are replaced with random alphanumeric characters)

```bash
mktemp /tmp/example.XXXXXXXX
```

### Use a custom file name prefix

```bash
mktemp -t example
```

### Create an empty temporary directory and print its absolute path

```bash
mktemp --directory
```
