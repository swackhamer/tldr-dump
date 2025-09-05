# pstopnm

> Convert a PostScript file to a PNM image. More information: <https://netpbm.sourceforge.net/doc/pstopnm.html>.

## Examples

### Convert a PS file to PNM images, storing page N of the input to `path/to/fileN.ppm`

```bash
pstopnm path/to/file.ps
```

### Explicitly specify the output format

```bash
pstopnm -pbm|pgm|ppm path/to/file.ps
```

### Specify the resolution of the output in dots per inch

```bash
pstopnm -dpi n path/to/file.ps
```
