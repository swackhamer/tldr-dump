# lzop

> Compress or decompress files with LZO compression. More information: <https://www.lzop.org/lzop_man.php>.

## Examples

### Compress a file into a new file with the `.lzo` suffix

```bash
lzop path/to/file
```

### Decompress a file

```bash
lzop [-d|--decompress] path/to/file.lzo
```

### Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3)

```bash
lzop -level path/to/file
```

### Compress a file with the best compression level

```bash
lzop [-9|--best] path/to/file
```

### Compress a file with the fastest compression level

```bash
lzop [-1|--fast] path/to/file
```
