# objdump

> View information about object files. More information: <https://manned.org/objdump>.

## Examples

### Display the file header information

```bash
objdump [-f|--file-headers] path/to/binary
```

### Display all header information

```bash
objdump [-x|--all-headers] path/to/binary
```

### Display the disassembled output of executable sections

```bash
objdump [-d|--disassemble] path/to/binary
```

### Display the disassembled executable sections in Intel syntax

```bash
objdump [-M|--disassembler-options] intel [-d|--disassemble] path/to/binary
```

### Display the symbol table

```bash
objdump [-t|--syms] path/to/binary
```

### Display a complete binary hex dump of all sections

```bash
objdump [-s|--full-contents] path/to/binary
```
