# ppmtobmp

> Convert a PPM image to a BMP file. More information: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

## Examples

### Convert a PPM image to a BMP file

```bash
ppmtobmp path/to/file.ppm > path/to/file.bmp
```

### Explicitly specify whether or not a Windows BMP file or an OS/2 BMP file should be created

```bash
ppmtobmp -windows|os2 path/to/file.ppm > path/to/file.bmp
```

### Use a specific number of bits for each pixel

```bash
ppmtobmp [-b|-bbp] 1|4|8|24 path/to/file.ppm > path/to/file.bmp
```
