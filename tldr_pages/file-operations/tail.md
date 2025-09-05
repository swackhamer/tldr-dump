# tail

> Display the last part of a file. See also: `head`. More information: <https://keith.github.io/xcode-man-pages/tail.1.html>.

## Examples

### Show last 'count' lines in file

```bash
tail -n 8 path/to/file
```

### Print a file from a specific line number

```bash
tail -n +8 path/to/file
```

### Print a specific count of bytes from the end of a given file

```bash
tail -c 8 path/to/file
```

### Print the last lines of a given file and keep reading it until `<Ctrl c>`

```bash
tail -f path/to/file
```

### Keep reading file until `<Ctrl c>`, even if the file is inaccessible

```bash
tail -F path/to/file
```

### Show last 'count' lines in 'file' and refresh every 'seconds' seconds

```bash
tail -n 8 -s 10 -f path/to/file
```
