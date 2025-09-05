# nm

> List symbol names in object files. More information: <https://manned.org/nm>.

## Examples

### List global (extern) functions in a file (prefixed with T)

```bash
nm [-g|--extern-only] path/to/file.o
```

### List only undefined symbols in a file

```bash
nm [-u|--undefined-only] path/to/file.o
```

### List all symbols, even debugging symbols

```bash
nm [-a|--debug-syms] path/to/file.o
```

### Demangle C++ symbols (make them readable)

```bash
nm [-C|--demangle] path/to/file.o
```
