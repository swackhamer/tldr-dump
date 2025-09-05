# pnmtoddif

> Convert a PNM image to a DDIF image file. More information: <https://netpbm.sourceforge.net/doc/pnmtoddif.html>.

## Examples

### Convert a PNM image to a DDIF image file

```bash
pnmtoddif path/to/image.pnm > path/to/image.ddif
```

### Explicitly specify the horizontal and vertical resolution of the output image

```bash
pnmtoddif [-r|-resolution] horizontal_dpi vertical_dpi path/to/image.pnm > path/to/image.ddif
```
