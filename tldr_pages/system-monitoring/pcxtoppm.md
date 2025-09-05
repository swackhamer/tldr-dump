# pcxtoppm

> Convert a PCX file to a PPM image. More information: <https://netpbm.sourceforge.net/doc/pcxtoppm.html>.

## Examples

### Convert a PCX file to a PPM image

```bash
pcxtoppm path/to/file.pcx > path/to/file.ppm
```

### Use a predefined standard palette even if the PCX file provides one

```bash
pcxtoppm [-s|-stdpalette] path/to/file.pcx > path/to/file.ppm
```

### Print information on the PCX header to `stdout`

```bash
pcxtoppm [-verb|-verbose] path/to/file.pcx > path/to/file.ppm
```
