# bison

> GNU parser generator. More information: <https://manned.org/bison>.

## Examples

### Compile a bison definition file

```bash
bison path/to/file.y
```

### Compile in debug mode, which causes the resulting parser to write additional information to `stdout`

```bash
bison [-t|--debug] path/to/file.y
```

### Specify the output filename

```bash
bison [-o|--output] path/to/output.c path/to/file.y
```

### Be verbose when compiling

```bash
bison [-v|--verbose]
```
