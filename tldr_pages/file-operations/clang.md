# clang

> Compile C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC. Part of LLVM. More information: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

## Examples

### Compile multiple source files into an executable

```bash
clang path/to/source1.c path/to/source2.c ... [-o|--output] path/to/output_executable
```

### Activate output of all errors and warnings

```bash
clang path/to/source.c -Wall [-o|--output] output_executable
```

### Show common warnings, debug symbols in output, and optimize without affecting debugging

```bash
clang path/to/source.c -Wall [-g|--debug] -Og [-o|--output] path/to/output_executable
```

### Include libraries from a different path

```bash
clang path/to/source.c [-o|--output] path/to/output_executable -Ipath/to/header -Lpath/to/library -llibrary_name
```

### Compile source code into LLVM Intermediate Representation (IR)

```bash
clang [-S|--assemble] -emit-llvm path/to/source.c [-o|--output] path/to/output.ll
```

### Compile source code into an object file without linking

```bash
clang [-c|--compile] path/to/source.c
```

### Optimize the compiled program for performance

```bash
clang path/to/source.c -O1|2|3|fast [-o|--output] path/to/output_executable
```

### Display version

```bash
clang --version
```
