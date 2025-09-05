# stat

> Display file status. More information: <https://keith.github.io/xcode-man-pages/stat.1.html>.

## Examples

### Show file properties such as size, permissions, creation and access dates among others

```bash
stat path/to/file
```

### Same as above but verbose (more similar to Linux's `stat`)

```bash
stat -x path/to/file
```

### Show only octal file permissions

```bash
stat -f %Mp%Lp path/to/file
```

### Show owner and group of the file

```bash
stat -f "%Su %Sg" path/to/file
```

### Show the size of the file in bytes

```bash
stat -f "%z %N" path/to/file
```
