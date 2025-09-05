# llvm-dis

> Convert LLVM bitcode files into human-readable LLVM Intermediate Representation (IR). More information: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

## Examples

### Convert a bitcode file as LLVM IR and write the result to `stdout`

```bash
llvm-dis path/to/input.bc -o -
```

### Convert a bitcode file to an LLVM IR file with the same filename

```bash
llvm-dis path/to/file.bc
```

### Convert a bitcode file to LLVM IR, writing the result to the specified file

```bash
llvm-dis path/to/input.bc -o path/to/output.ll
```
