# fold

> Wrap each line in an input file to fit a specified width and print it to `stdout`. More information: <https://manned.org/fold.1p>.

## Examples

### Wrap each line to default width (80 characters)

```bash
fold path/to/file
```

### Wrap each line to width "30"

```bash
fold -w30 path/to/file
```

### Wrap each line to width "5" and break the line at spaces (puts each space separated word in a new line, words with length > 5 are wrapped)

```bash
fold -w5 -s path/to/file
```
