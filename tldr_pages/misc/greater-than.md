# greater-than

> Redirect output. More information: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Output>.

## Examples

### Redirect `stdout` to a file

```bash
command > path/to/file
```

### Append to a file

```bash
command >> path/to/file
```

### Redirect both `stdout` and `stderr` to a file

```bash
command &> path/to/file
```

### Redirect `stderr` to `/dev/null` to keep the terminal output clean

```bash
command 2> /dev/null
```

### Clear the file contents or create a new empty file

```bash
> path/to/file
```

### Redirect `stderr` to `stdout` for piping them together

```bash
command1 2>&1 | command2
```

### Open a persistent file descriptor

```bash
exec 3>path/to/file
```

### Write to a custom file descriptor

```bash
echo text >&3
```
