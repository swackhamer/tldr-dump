# unrar

> Extract RAR archives. More information: <https://manned.org/unrar>.

## Examples

### Extract files with original directory structure

```bash
unrar x compressed.rar
```

### Extract files to a specified path with the original directory structure

```bash
unrar x compressed.rar path/to/extract
```

### Extract files into current directory, losing directory structure in the archive

```bash
unrar e compressed.rar
```

### Test integrity of each file inside the archive file

```bash
unrar t compressed.rar
```

### List files inside the archive file without decompressing it

```bash
unrar l compressed.rar
```
