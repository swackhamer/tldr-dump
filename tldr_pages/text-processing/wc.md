# wc

> Count lines, words, or bytes. More information: <https://keith.github.io/xcode-man-pages/wc.1.html>.

## Examples

### Count lines in file

```bash
wc -l path/to/file
```

### Count words in file

```bash
wc -w path/to/file
```

### Count characters (bytes) in file

```bash
wc -c path/to/file
```

### Count characters in file (taking multi-byte character sets into account)

```bash
wc -m path/to/file
```

### Use `stdin` to count lines, words and characters (bytes) in that order

```bash
find . | wc
```
