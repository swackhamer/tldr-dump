# fiascotopnm

> Convert a compressed FIASCO file to a PNM image. More information: <https://netpbm.sourceforge.net/doc/fiascotopnm.html>.

## Examples

### Convert a compressed FIASCO file to a PNM file or in the case of video streams multiple PNM files

```bash
fiascotopnm path/to/file.fiasco [-o|--output] output_file_basename
```

### Use fast decompression, resulting in a slightly decreased quality of the output file(s)

```bash
fiascotopnm [-z|--fast] path/to/file.fiasco [-o|--output] output_file_basename
```

### Load the options to be used from the specified configuration file

```bash
fiascotopnm [-f|--config] path/to/fiascorc path/to/file.fiasco [-o|--output] output_file_basename
```

### Magnify the decompressed image(s) by a factor of 2^n

```bash
fiascotopnm [-m|--magnify] n path/to/file.fiasco [-o|--output] output_file_basename
```

### Smooth the decompressed image by the specified amount

```bash
fiascotopnm [-s|--smoothing] n path/to/file.fiasco [-o|--output] output_file_basename
```
