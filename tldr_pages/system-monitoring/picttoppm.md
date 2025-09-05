# picttoppm

> Convert a Macintosh PICT file to a PPM image. More information: <https://netpbm.sourceforge.net/doc/picttoppm.html>.

## Examples

### Convert a PICT file to a PPM image

```bash
picttoppm path/to/file.pict > path/to/file.ppm
```

### Force any images in the PICT file to be output at full resolution

```bash
picttoppm [-fu|-fullres] path/to/file.pict > path/to/file.ppm
```

### Do not assume that the input file contains a PICT header and execute quickdraw operations only

```bash
picttoppm [-n|-noheader] [-quic|-quickdraw] path/to/file.pict > path/to/file.ppm
```
