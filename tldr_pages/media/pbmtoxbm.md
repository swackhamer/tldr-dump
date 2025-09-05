# pbmtoxbm

> Convert a PBM image to a X11 or X10 bitmap. More information: <https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

## Examples

### Convert a PBM image to a X11 XBM file

```bash
pbmtoxbm path/to/input_file.pbm > path/to/output_file.xbm
```

### Explicitly specify whether an X11 or X10 bitmap should be generated

```bash
pbmtoxbm -x11|x10 path/to/input_file.pbm > path/to/output_file.xbm
```
