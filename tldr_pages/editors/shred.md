# shred

> Overwrite files to securely delete data. More information: <https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

## Examples

### Overwrite a file

```bash
shred path/to/file
```

### Overwrite a file and show progress on the screen

```bash
shred [-v|--verbose] path/to/file
```

### Overwrite a file, leaving zeros instead of random data

```bash
shred [-z|--zero] path/to/file
```

### Overwrite a file a specific number of times

```bash
shred [-n|--iterations] 25 path/to/file
```

### Overwrite a file and remove it

```bash
shred [-u|--remove] path/to/file
```

### Overwrite a file 100 times, add a final overwrite with zeros, remove the file after overwriting it and show verbose progress on the screen

```bash
shred [-vzun|--verbose --zero --remove --iterations] 100 path/to/file
```
