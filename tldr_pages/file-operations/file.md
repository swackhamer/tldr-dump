# file

> Determine file type. More information: <https://manned.org/file>.

## Examples

### Give a description of the type of the specified file. Works fine for files with no file extension

```bash
file path/to/file
```

### Look inside a zipped file and determine the file type(s) inside

```bash
file [-z|--uncompress] foo.zip
```

### Allow file to work with special or device files

```bash
file [-s|--special-files] path/to/file
```

### Don't stop at first file type match; keep going until the end of the file

```bash
file [-k|--keep-going] path/to/file
```

### Determine the MIME encoding type of a file

```bash
file [-i|--mime] path/to/file
```
