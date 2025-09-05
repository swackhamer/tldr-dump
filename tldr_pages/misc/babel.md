# babel

> A transpiler which converts code from JavaScript ES6/ES7 syntax to ES5 syntax. More information: <https://babeljs.io/docs/babel-cli>.

## Examples

### Transpile a specified input file and output to `stdout`

```bash
babel path/to/file
```

### Transpile a specified input file and output to a specific file

```bash
babel path/to/input_file --out-file path/to/output_file
```

### Transpile the input file every time it is changed

```bash
babel path/to/input_file --watch
```

### Transpile a whole directory of files

```bash
babel path/to/input_directory
```

### Ignore specified comma-separated files in a directory

```bash
babel path/to/input_directory --ignore ignored_file1,ignored_file2,...
```

### Transpile and output as minified JavaScript

```bash
babel path/to/input_file --minified
```

### Choose a set of presets for output formatting

```bash
babel path/to/input_file --presets preset1,preset2,...
```

### Display help

```bash
babel --help
```
