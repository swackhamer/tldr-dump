# ldc

> D compiler using LLVM as a backend. More information: <https://wiki.dlang.org/Using_LDC>.

## Examples

### Compile a source code file into an executable binary

```bash
ldc2 path/to/source.d -of=path/to/output_executable
```

### Compile the source code file without linking

```bash
ldc2 -c path/to/source.d
```

### Select the target architecture and OS

```bash
ldc -mtriple=architecture_OS -c path/to/source.d
```

### Display help

```bash
ldc2 -h
```

### Display complete help

```bash
ldc2 -help-hidden
```
