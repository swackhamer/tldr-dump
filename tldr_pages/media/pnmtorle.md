# pnmtorle

> Convert a PNM file to an Utah Raster Tools RLE image file. More information: <https://netpbm.sourceforge.net/doc/pnmtorle.html>.

## Examples

### Convert a PNM image to an RLE image

```bash
pnmtorle path/to/input.pnm > path/to/output.rle
```

### Print PNM header information to `stdout`

```bash
pnmtorle [-verb|-verbose] path/to/input.pnm > path/to/output.rle
```

### Include a transparency channel in the output image in which every black pixel is set to fully transparent and every other pixel is set to fully opaque

```bash
pnmtorle [-a|-alpha] path/to/input.pnm > path/to/output.rle
```
