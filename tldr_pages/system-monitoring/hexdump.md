# hexdump

> Display file contents in hexadecimal, decimal, octal, or ASCII. Useful for inspecting dump file, binary data, or debug output. See also: `hexyl`, `od`, `xxd`. More information: <https://manned.org/man/freebsd/hexdump.1>.

## Examples

### Print the hexadecimal representation of a file, replacing duplicate lines by `*`

```bash
hexdump path/to/file
```

### Display the input offset in hexadecimal and its ASCII representation in two columns

```bash
hexdump -C path/to/file
```

### Display the hexadecimal representation of a file, but interpret only a specific number of bytes of the input

```bash
hexdump -C -n number_of_bytes path/to/file
```

### Verbose - no suppression by `*` on duplicate lines

```bash
hexdump -v path/to/file
```

### Format output using printf-like format string

```bash
hexdump -e 'element_format .. end_format' path/to/file
```
