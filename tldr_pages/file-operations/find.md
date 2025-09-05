# find

> Find files or directories under a directory tree, recursively. More information: <https://manned.org/find>.

## Examples

### Find files by extension

```bash
find root_path -name '*.ext'
```

### Find files matching multiple path/name patterns

```bash
find root_path -path '*/path/*/*.ext' -or -name '*pattern*'
```

### Find directories matching a given name, in case-insensitive mode

```bash
find root_path -type d -iname '*lib*'
```

### Find files matching a given pattern, excluding specific paths

```bash
find root_path -name '*.py' -not -path '*/site-packages/*'
```

### Find files matching a given size range, limiting the recursive depth to "1"

```bash
find root_path -maxdepth 1 -size +500k -size -10M
```

### Run a command for each file (use `{}` within the command to access the filename)

```bash
find root_path -name '*.ext' -exec wc -l {} \;
```

### Find all files modified today and pass the results to a single command as arguments

```bash
find root_path -daystart -mtime -1 -exec tar -cvf archive.tar {} \+
```

### Search for either empty files or directories and delete them verbosely

```bash
find root_path -type f|d -empty -delete -print
```
