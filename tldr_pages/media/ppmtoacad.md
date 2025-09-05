# ppmtoacad

> Convert a PPM image to an AutoCAD database or slide. More information: <https://netpbm.sourceforge.net/doc/ppmtoacad.html>.

## Examples

### Convert a PPM image to an AutoCAD slide

```bash
ppmtoacad path/to/file.ppm > path/to/file.acad
```

### Convert a PPM image to an AutoCAD binary database import file

```bash
ppmtoacad [-d|-dxb] path/to/file.ppm > path/to/file.dxb
```

### Restrict the colors in the output to 8 RGB shades

```bash
ppmtoacad -8 path/to/file.ppm > path/to/file.dxb
```
