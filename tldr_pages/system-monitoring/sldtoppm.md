# sldtoppm

> Convert an AutoCAD slide file to a PPM image. More information: <https://netpbm.sourceforge.net/doc/sldtoppm.html>.

## Examples

### Convert an SLD file to a PPM image

```bash
sldtoppm path/to/input.sld > path/to/output.ppm
```

### Compensate for non-square pixels by scaling the width of the image

```bash
sldtoppm [-a|-adjust] path/to/input.sld > path/to/output.ppm
```
