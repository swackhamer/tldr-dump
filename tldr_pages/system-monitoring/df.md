# df

> Display an overview of the filesystem disk space usage. More information: <https://keith.github.io/xcode-man-pages/df.1.html>.

## Examples

### Display all filesystems and their disk usage using 512-byte units

```bash
df
```

### Use [h]uman-readable units (based on powers of 1024) and display a grand total

```bash
df -h -c
```

### Use [H]uman-readable units (based on powers of 1000)

```bash
df --si|H
```

### Display the filesystem and its disk usage containing the given file or directory

```bash
df path/to/file_or_directory
```

### Include statistics on the number of free and used [i]nodes including the filesystem t[Y]pes

```bash
df -iY
```

### Use 1024-byte units when writing space figures

```bash
df -k
```

### Display information in a [P]ortable way

```bash
df -P
```
