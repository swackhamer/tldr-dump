# pnmtofiasco

> Convert a PNM image to a compressed FIASCO file. More information: <https://netpbm.sourceforge.net/doc/pnmtofiasco.html>.

## Examples

### Convert a PNM image to a compressed FIASCO file

```bash
pnmtofiasco path/to/file.pnm > path/to/file.fiasco
```

### Specify the input files through a pattern

```bash
pnmtofiasco [-i|--image-name] "img[01-09+1].pnm" > path/to/file.fiasco
```

### Specify the compression quality

```bash
pnmtofiasco [-q|--quality] quality_level path/to/file.pnm > path/to/file.fiasco
```

### Load the options to be used from the specified configuration file

```bash
pnmtofiasco [-f|--config] path/to/fiascorc path/to/file.pnm > path/to/file.fiasco
```
