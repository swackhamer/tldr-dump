# g++

> Compile C++ source files. Part of GCC (GNU Compiler Collection). More information: <https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html>.

## Examples

### Compile a source code file into an executable binary

```bash
g++ path/to/source1.cpp path/to/source2.cpp ... [-o|--output] path/to/output_executable
```

### Activate output of all errors and warnings

```bash
g++ path/to/source.cpp -Wall [-o|--output] output_executable
```

### Show common warnings, debug symbols in output, and optimize without affecting debugging

```bash
g++ path/to/source.cpp -Wall [-g|--debug] -Og [-o|--output] path/to/output_executable
```

### Choose a language standard to compile for (C++98/C++11/C++14/C++17)

```bash
g++ path/to/source.cpp -std=c++98|c++11|c++14|c++17 [-o|--output] path/to/output_executable
```

### Include libraries located at a different path than the source file

```bash
g++ path/to/source.cpp [-o|--output] path/to/output_executable -Ipath/to/header -Lpath/to/library -llibrary_name
```

### Compile and link multiple source code files into an executable binary

```bash
g++ [-c|--compile] path/to/source1.cpp path/to/source2.cpp ... && g++ [-o|--output] path/to/output_executable path/to/source1.o path/to/source2.o ...
```

### Optimize the compiled program for performance

```bash
g++ path/to/source.cpp -O1|2|3|fast [-o|--output] path/to/output_executable
```

### Display version

```bash
g++ --version
```
