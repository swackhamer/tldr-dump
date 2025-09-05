# lzip

> A lossless data compressor with a user interface similar to `gzip` or `bzip2`. Lzip uses a simplified form of the "Lempel-Ziv-Markovchain-Algorithm" (LZMA) stream format and provides 3-factor integrity checking to maximize interoperability and optimize safety. More information: <https://www.nongnu.org/lzip/manual/lzip_manual.html#Invoking-lzip>.

## Examples

### Archive a file, replacing it with with a compressed version

```bash
lzip path/to/file
```

### Archive a file, keeping the input file

```bash
lzip [-k|--keep] path/to/file
```

### Archive a file with the best compression (level=9)

```bash
lzip [-k|--keep] path/to/file --best
```

### Archive a file at the fastest speed (level=0)

```bash
lzip [-k|--keep] path/to/file --fast
```

### Test the integrity of compressed file

```bash
lzip [-t|--test] path/to/archive.lz
```

### Decompress a file, replacing it with the original uncompressed version

```bash
lzip [-d|--decompress] path/to/archive.lz
```

### Decompress a file, keeping the archive

```bash
lzip [-d|--decompress] [-k|--keep] path/to/archive.lz
```

### List files which are in an archive and show compression stats

```bash
lzip [-l|--list] path/to/archive.lz
```
