# isutf8

> Check whether text files contain valid UTF-8. More information: <https://manned.org/isutf8>.

## Examples

### Check whether the specified files contain valid UTF-8

```bash
isutf8 path/to/file1 path/to/file2 ...
```

### Print errors using multiple lines

```bash
isutf8 [-v|--verbose] path/to/file1 path/to/file2 ...
```

### Do not print anything to `stdout`, indicate the result merely with the exit code

```bash
isutf8 [-q|--quiet] path/to/file1 path/to/file2 ...
```

### Only print the names of the files containing invalid UTF-8

```bash
isutf8 [-l|--list] path/to/file1 path/to/file2 ...
```

### Same as `--list` but inverted, i.e., only print the names of the files containing valid UTF-8

```bash
isutf8 [-i|--invert] path/to/file1 path/to/file2 ...
```
