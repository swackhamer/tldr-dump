# gdc

> D compiler using GCC as a backend. More information: <https://wiki.dlang.org/Using_GDC>.

## Examples

### Create an executable

```bash
gdc path/to/source.d -o path/to/output_executable
```

### Print information about module dependencies

```bash
gdc -fdeps
```

### Generate Ddoc documentation

```bash
gdc -fdoc
```

### Generate D interface files

```bash
gdc -fintfc
```

### Do not link the standard GCC libraries in the compilation

```bash
gdc -nostdlib
```
