# lebab

> A JavaScript modernizer for transpiling code to ES6/ES7. Transformations must be provided for all examples. More information: <https://github.com/lebab/lebab>.

## Examples

### Transpile using one or more comma-separated transformations

```bash
lebab --transform transformation1,transformation2,...
```

### Transpile a file to `stdout`

```bash
lebab path/to/input_file
```

### Transpile a file to the specified output file

```bash
lebab path/to/input_file --out-file path/to/output_file
```

### Replace all `.js` files in-place in the specified directory, glob or file

```bash
lebab --replace directory|glob|file
```

### Display help

```bash
lebab --help
```
