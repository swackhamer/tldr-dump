# lpstat

> Display status information about the current classes, jobs, and printers. More information: <https://keith.github.io/xcode-man-pages/lpstat.1.html>.

## Examples

### Show a long listing of printers, classes, and jobs

```bash
lpstat -l
```

### Force encryption when connecting to the CUPS server

```bash
lpstat -E
```

### Show the ranking of print jobs

```bash
lpstat -R
```

### Show whether or not the CUPS server is running

```bash
lpstat -r
```

### Show all status information

```bash
lpstat -t
```
