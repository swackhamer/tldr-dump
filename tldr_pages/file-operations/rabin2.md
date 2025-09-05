# rabin2

> Get information about binary files (ELF, PE, Java CLASS, Mach-O) - symbols, sections, linked libraries, etc. Comes bundled with `radare2`. More information: <https://manned.org/rabin2>.

## Examples

### Display general information about a binary (architecture, type, endianness)

```bash
rabin2 -I path/to/binary
```

### Display linked libraries

```bash
rabin2 -l path/to/binary
```

### Display symbols imported from libraries

```bash
rabin2 -i path/to/binary
```

### Display strings contained in the binary

```bash
rabin2 -z path/to/binary
```

### Display the output in JSON

```bash
rabin2 -j -I path/to/binary
```
