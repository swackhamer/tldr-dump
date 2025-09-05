# wasm-objdump

> Display information from WebAssembly binaries. More information: <https://github.com/WebAssembly/wabt>.

## Examples

### Display the section headers of a given binary

```bash
wasm-objdump [-h|--headers] file.wasm
```

### Display the entire disassembled output of a given binary

```bash
wasm-objdump [-d|--disassemble] file.wasm
```

### Display the details of each section

```bash
wasm-objdump [-x|--details] file.wasm
```

### Display the details of a given section

```bash
wasm-objdump [-j|--section] 'import' [-x|--details] file.wasm
```
