# pbmtoepsi

> Convert a PBM image to an encapsulated PostScript style preview bitmap. More information: <https://netpbm.sourceforge.net/doc/pbmtoepsi.html>.

## Examples

### Convert a PBM image to an encapsulated PostScript style preview bitmap

```bash
pbmtoepsi path/to/image.pbm > path/to/output.bmp
```

### Produce a quadratic output image with the specified resolution

```bash
pbmtoepsi [-d|-dpi] 144 path/to/image.pbm > path/to/output.bmp
```

### Produce an output image with the specified horizontal and vertical resolution

```bash
pbmtoepsi [-d|-dpi] 72x144 path/to/image.pbm > path/to/output.bmp
```

### Only create a boundary box

```bash
pbmtoepsi [-b|-bbonly] path/to/image.pbm > path/to/output.bmp
```
