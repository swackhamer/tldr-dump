# truncate

> Shrink or extend the size of a file to the specified size. More information: <https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html>.

## Examples

### Set a size of 10 GB to an existing file, or create a new file with the specified size

```bash
truncate [-s|--size] 10G path/to/file
```

### Extend the file size by 50 MiB, fill with holes (which reads as zero bytes)

```bash
truncate [-s|--size] +50M path/to/file
```

### Shrink the file by 2 GiB, by removing data from the end of file

```bash
truncate [-s|--size] -2G path/to/file
```

### Empty the file's content

```bash
truncate [-s|--size] 0 path/to/file
```

### Empty the file's content, but do not create the file if it does not exist

```bash
truncate [-cs|--no-create --size] 0 path/to/file
```
