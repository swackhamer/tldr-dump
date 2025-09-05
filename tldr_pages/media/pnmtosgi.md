# pnmtosgi

> Convert a PNM file to an SGI image file. More information: <https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

## Examples

### Convert a PNM image to an SGI image

```bash
pnmtosgi path/to/input.pnm > path/to/output.sgi
```

### Disable or enable compression

```bash
pnmtosgi -verbatim|rle path/to/input.pnm > path/to/output.sgi
```

### Write the specified string into the SGI image header's `imagename` field

```bash
pnmtosgi [-i|-imagename] string path/to/input.pnm > path/to/output.sgi
```
