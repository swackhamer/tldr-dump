# ect

> Efficient Compression Tool. File optimizer written in C++. It supports PNG, JPEG, gzip and Zip files. More information: <https://github.com/fhanau/Efficient-Compression-Tool>.

## Examples

### Compress a file

```bash
ect path/to/file.png
```

### Compress a file with specified compression level and multithreading (1=Fastest (Worst), 9=Slowest (Best), default is 3)

```bash
ect -9 --mt-deflate path/to/file.zip
```

### Compress all files in a directory recursively

```bash
ect -recurse path/to/directory
```

### Compress a file, keeping the original modification time

```bash
ect -keep path/to/file.png
```

### Compress a file, stripping metadata

```bash
ect -strip path/to/file.png
```
