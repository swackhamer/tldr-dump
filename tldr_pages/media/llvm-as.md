# llvm-as

> LLVM Intermediate Representation (`.ll`) to Bitcode (`.bc`) assembler. More information: <https://llvm.org/docs/CommandGuide/llvm-as.html>.

## Examples

### Assemble an IR file

```bash
llvm-as -o path/to/out.bc path/to/source.ll
```

### Assemble an IR file and include a module hash in the produced Bitcode file

```bash
llvm-as --module-hash -o path/to/out.bc path/to/source.ll
```

### Read an IR file from `stdin` and assemble it

```bash
cat path/to/source.ll | llvm-as -o path/to/out.bc
```
