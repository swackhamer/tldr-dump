# du

> Disk usage: estimate and summarize file and directory space usage. More information: <https://keith.github.io/xcode-man-pages/du.1.html>.

## Examples

### List the sizes of a directory and any subdirectories, in the given unit (KiB/MiB/GiB)

```bash
du -k|m|g path/to/directory
```

### List the sizes of a directory and any subdirectories, in human-readable form (i.e. auto-selecting the appropriate unit for each size)

```bash
du -h path/to/directory
```

### Show the size of a single directory, in human-readable units

```bash
du -sh path/to/directory
```

### List the human-readable sizes of a directory and of all the files and directories within it

```bash
du -ah path/to/directory
```

### List the human-readable sizes of a directory and any subdirectories, up to N levels deep

```bash
du -h -d 2 path/to/directory
```

### List the human-readable size of all `.jpg` files in subdirectories of the current directory, and show a cumulative total at the end

```bash
du -ch */*.jpg
```
