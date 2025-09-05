# pigz

> Multithreaded zlib compression utility. More information: <https://github.com/madler/pigz>.

## Examples

### Compress a file with default options

```bash
pigz path/to/file
```

### Compress a file using the best compression method

```bash
pigz [-9|--best] path/to/file
```

### Compress a file using no compression and 4 processors

```bash
pigz -0 [-p|--processes] 4 path/to/file
```

### Compress a directory using tar

```bash
tar cf - path/to/directory | pigz > path/to/file.tar.gz
```

### Decompress a file

```bash
pigz [-d|--decompress] archive.gz
```

### List the contents of an archive

```bash
pigz [-l|--list] archive.tar.gz
```
