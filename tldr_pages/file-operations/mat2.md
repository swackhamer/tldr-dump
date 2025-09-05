# mat2

> Anonymise various file formats by removing metadata. More information: <https://0xacab.org/jvoisin/mat2>.

## Examples

### List supported file formats

```bash
mat2 --list
```

### Remove metadata from a file

```bash
mat2 path/to/file
```

### Remove metadata from a file and print detailed output to the console

```bash
mat2 --verbose path/to/file
```

### Show metadata in a file without removing it

```bash
mat2 --show path/to/file
```

### Partially remove metadata from a file

```bash
mat2 --lightweight path/to/file
```

### Remove metadata from a file in place, without creating a backup

```bash
mat2 --inplace path/to/file
```
