# wasm-opt

> Optimize WebAssembly binary files. More information: <https://github.com/webassembly/binaryen>.

## Examples

### Apply default optimizations and write to a given file

```bash
wasm-opt -O input.wasm [-o|--output] output.wasm
```

### Apply all optimizations and write to a given file (takes more time, but generates optimal code)

```bash
wasm-opt -O4 input.wasm [-o|--output] output.wasm
```

### Optimize a file for size

```bash
wasm-opt -Oz input.wasm [-o|--output] output.wasm
```

### Print the textual representation of the binary to console

```bash
wasm-opt input.wasm --print
```
