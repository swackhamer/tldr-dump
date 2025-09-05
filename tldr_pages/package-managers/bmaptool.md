# bmaptool

> Create or copy block maps intelligently (designed to be faster than `cp` or `dd`). More information: <https://manned.org/bmaptool>.

## Examples

### Output a blockmap file from image file

```bash
bmaptool create [-o|--output] blockmap.bmap source.img
```

### Copy an image file into sdb

```bash
bmaptool copy --bmap blockmap.bmap source.img /dev/sdb
```

### Copy a compressed image file into sdb

```bash
bmaptool copy --bmap blockmap.bmap source.img.gz /dev/sdb
```

### Copy an image file into sdb without using a blockmap

```bash
bmaptool copy --nobmap source.img /dev/sdb
```
