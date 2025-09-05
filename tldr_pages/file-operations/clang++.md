# clang++

> Compile C++ source files. Part of LLVM. More information: <https://clang.llvm.org>.

## Examples

### Compile a set of source code files into an executable binary

```bash
clang++ path/to/source1.cpp path/to/source2.cpp ... [-o|--output] path/to/output_executable
```

### Activate output of all errors and warnings

```bash
clang++ path/to/source.cpp -Wall [-o|--output] output_executable
```

### Show common warnings, debug symbols in output, and optimize without affecting debugging

```bash
clang++ path/to/source.cpp -Wall [-g|--debug] -Og [-o|--output] path/to/output_executable
```

### Choose a language standard to compile for

```bash
clang++ path/to/source.cpp -std=c++20 [-o|--output] path/to/output_executable
```

### Include libraries located at a different path than the source file

```bash
clang++ path/to/source.cpp [-o|--output] path/to/output_executable -Ipath/to/header_path -Lpath/to/library_path -lpath/to/library_name
```

### Compile source code into LLVM Intermediate Representation (IR)

```bash
clang++ [-S|--assemble] -emit-llvm path/to/source.cpp [-o|--output] path/to/output.ll
```

### Optimize the compiled program for performance

```bash
clang++ path/to/source.cpp -O1|2|3|fast [-o|--output] path/to/output_executable
```

### Display version

```bash
clang++ --version
```
