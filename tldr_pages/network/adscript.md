# adscript

> Compiler for Adscript files. More information: <https://github.com/Amplus2/Adscript>.

## Examples

### Compile a file to an object file

```bash
adscript --output path/to/file.o path/to/input_file.adscript
```

### Compile and link a file to a standalone executable

```bash
adscript --executable --output path/to/file path/to/input_file.adscript
```

### Compile a file to LLVM IR instead of native machine code

```bash
adscript --llvm-ir --output path/to/file.ll path/to/input_file.adscript
```

### Cross-compile a file to an object file for a foreign CPU architecture or operating system

```bash
adscript --target-triple i386-linux-elf --output path/to/file.o path/to/input_file.adscript
```
