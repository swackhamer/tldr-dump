# gfortran

> Preprocess and compile Fortran source files, then assemble and link them together. More information: <https://gcc.gnu.org/onlinedocs/gfortran/Invoking-GNU-Fortran.html>.

## Examples

### Compile multiple source files into an executable

```bash
gfortran path/to/source1.f90 path/to/source2.f90 ... -o path/to/output_executable
```

### Show common warnings, debug symbols in output, and optimize without affecting debugging

```bash
gfortran path/to/source.f90 -Wall -g -Og -o path/to/output_executable
```

### Include libraries from a different path

```bash
gfortran path/to/source.f90 -o path/to/output_executable -Ipath/to/mod_and_include -Lpath/to/library -llibrary_name
```

### Compile source code into Assembler instructions

```bash
gfortran -S path/to/source.f90
```

### Compile source code into an object file without linking

```bash
gfortran -c path/to/source.f90
```
