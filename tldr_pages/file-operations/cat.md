# cat

> Print and concatenate files. More information: <https://keith.github.io/xcode-man-pages/cat.1.html>.

## Examples

### Print the contents of a file to `stdout`

```bash
cat path/to/file
```

### Concatenate several files into an output file

```bash
cat path/to/file1 path/to/file2 ... > path/to/output_file
```

### Append several files to an output file

```bash
cat path/to/file1 path/to/file2 ... >> path/to/output_file
```

### Copy the contents of a file into an output file without buffering

```bash
cat -u /dev/tty12 > /dev/tty13
```

### Write `stdin` to a file

```bash
cat - > path/to/file
```

### Number all output lines

```bash
cat -n path/to/file
```

### Display non-printable and whitespace characters (with `M-` prefix if non-ASCII)

```bash
cat -v -t -e path/to/file
```
