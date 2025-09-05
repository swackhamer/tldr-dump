# head

> Output the first part of files. More information: <https://keith.github.io/xcode-man-pages/head.1.html>.

## Examples

### Output the first few lines of a file

```bash
head [-n|--lines] 8 path/to/file
```

### Output the first few bytes of a file

```bash
head [-c|--bytes] 8 path/to/file
```

### Output everything but the last few lines of a file

```bash
head [-n|--lines] -8 path/to/file
```

### Output everything but the last few bytes of a file

```bash
head [-c|--bytes] -8 path/to/file
```
