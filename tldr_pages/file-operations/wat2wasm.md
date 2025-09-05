# wat2wasm

> Convert a file from the WebAssembly text format to the binary format. More information: <https://github.com/WebAssembly/wabt>.

## Examples

### Parse and check a file for errors

```bash
wat2wasm file.wat
```

### Write the output binary to a given file

```bash
wat2wasm file.wat [-o|--output] file.wasm
```

### Display simplified representation of every byte

```bash
wat2wasm [-v|--verbose] file.wat
```
