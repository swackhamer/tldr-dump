# gcc

> Preprocess and compile C and C++ source files, then assemble and link them together. Part of GCC (GNU Compiler Collection). More information: <https://gcc.gnu.org/onlinedocs/gcc/>.

## Examples

### Compile multiple source files into an executable

```bash
gcc path/to/source1.c path/to/source2.c ... [-o|--output] path/to/output_executable
```

### Activate output of all errors and warnings

```bash
gcc path/to/source.c -Wall [-o|--output] output_executable
```

### Show common warnings, debug symbols in output, and optimize without affecting debugging

```bash
gcc path/to/source.c -Wall [-g|--debug] -Og [-o|--output] path/to/output_executable
```

### Include libraries from a different path

```bash
gcc path/to/source.c [-o|--output] path/to/output_executable -Ipath/to/header -Lpath/to/library -llibrary_name
```

### Compile source code into Assembler instructions

```bash
gcc [-S|--assemble] path/to/source.c
```

### Compile source code into an object file without linking

```bash
gcc [-c|--compile] path/to/source.c
```

### Optimize the compiled program for performance

```bash
gcc path/to/source.c -O1|2|3|fast [-o|--output] path/to/output_executable
```

### Display version

```bash
gcc --version
```
