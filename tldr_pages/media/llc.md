# llc

> Compiles LLVM Intermediate Representation or bitcode to target-specific assembly language. More information: <https://www.llvm.org/docs/CommandGuide/llc.html>.

## Examples

### Compile a bitcode or IR file to an assembly file with the same base name

```bash
llc path/to/file.ll
```

### Enable all optimizations

```bash
llc -O3 path/to/input.ll
```

### Output assembly to a specific file

```bash
llc --output path/to/output.s
```

### Emit fully relocatable, position independent code

```bash
llc -relocation-model=pic path/to/input.ll
```
