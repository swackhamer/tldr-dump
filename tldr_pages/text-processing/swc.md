# swc

> JavaScript and TypeScript compiler written in Rust. More information: <https://swc.rs>.

## Examples

### Transpile a specified input file and output to `stdout`

```bash
swc path/to/file
```

### Transpile the input file every time it is changed

```bash
swc path/to/file --watch
```

### Transpile a specified input file and output to a specific file

```bash
swc path/to/input_file --out-file path/to/output_file
```

### Transpile a specified input directory and output to a specific directory

```bash
swc path/to/input_directory --out-dir path/to/output_directory
```

### Transpile a specified input directory using a specific configuration file

```bash
swc path/to/input_directory --config-file path/to/.swcrc
```

### Ignore files in a directory specified using glob path

```bash
swc path/to/input_directory --ignore path/to/ignored_file1 path/to/ignored_file2 ...
```
