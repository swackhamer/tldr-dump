# gdu

> Disk usage analyzer with console interface. More information: <https://github.com/dundee/gdu>.

## Examples

### Interactively show the disk usage of the current directory

```bash
gdu
```

### Interactively show the disk usage of a given directory

```bash
gdu path/to/directory
```

### Interactively show the disk usage of all mounted disks

```bash
gdu --show-disks
```

### Interactively show the disk usage of the current directory but ignore some sub-directories

```bash
gdu --ignore-dirs path/to/directory1,path/to/directory2,...
```

### Ignore paths by `regex`

```bash
gdu --ignore-dirs-pattern '.*[abc]+'
```

### Ignore hidden directories

```bash
gdu --no-hidden
```

### Only print the result, do not enter interactive mode

```bash
gdu --non-interactive path/to/directory
```

### Do not show the progress in non-interactive mode (useful in scripts)

```bash
gdu --no-progress path/to/directory
```
