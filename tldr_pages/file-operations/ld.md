# ld

> Link object files together. More information: <https://sourceware.org/binutils/docs/ld.html>.

## Examples

### Link a specific object file with no dependencies into an executable

```bash
ld path/to/file.o [-o|--output] path/to/output_executable
```

### Link two object files together

```bash
ld path/to/file1.o path/to/file2.o [-o|--output] path/to/output_executable
```

### Dynamically link an x86_64 program to glibc (file paths change depending on the system)

```bash
ld [-o|--output] path/to/output_executable [-I|--dynamic-linker] /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc path/to/file.o /lib/crtn.o
```
