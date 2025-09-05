# rletopnm

> Convert a Utah Raster Tools RLE image file to a PNM file. More information: <https://netpbm.sourceforge.net/doc/rletopnm.html>.

## Examples

### Convert an RLE image to a PNM file

```bash
rletopnm path/to/input.rle > path/to/output.pnm
```

### Create a PGM image containing the RLE file's alpha channel

```bash
rletopnm [--a|--alphaout] path/to/alpha_file.pgm path/to/input.rle > path/to/output.pnm
```

### Operate in verbose mode and print the contents of the RLE header to `stdout`

```bash
rletopnm [--verb|--verbose] path/to/input.rle > path/to/output.pnm
```
