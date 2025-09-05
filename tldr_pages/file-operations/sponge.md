# sponge

> Soak up the input before writing the output file. More information: <https://manned.org/sponge>.

## Examples

### Append file content to the source file

```bash
cat path/to/file | sponge -a path/to/file
```

### Remove all lines starting with # in a file

```bash
grep [-v|--invert-match] '^#' path/to/file | sponge path/to/file
```
