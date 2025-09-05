# convmv

> Convert filenames (NOT file content) from one encoding to another. More information: <https://www.j3e.de/linux/convmv/man/>.

## Examples

### Test filename encoding conversion (don't actually change the filename)

```bash
convmv -f from_encoding -t to_encoding input_file
```

### Convert filename encoding and rename the file to the new encoding

```bash
convmv -f from_encoding -t to_encoding --notest input_file
```
