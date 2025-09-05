# tgatoppm

> Convert a TrueVision Targa file to a Netpbm image. More information: <https://netpbm.sourceforge.net/doc/tgatoppm.html>.

## Examples

### Convert a TrueVision Targa file to a PPM image

```bash
tgatoppm path/to/file.tga > path/to/output.ppm
```

### Dump information from the TGA header to `stdout`

```bash
tgatoppm [-h|-headerdump] path/to/file.tga > path/to/output.ppm
```

### Write the transparency channel values of the input image to the specified file

```bash
tgatoppm [-a|-alphaout] path/to/transparency_file.pgm path/to/file.tga > path/to/output.ppm
```

### Display version

```bash
tgatoppm [-v|-version]
```
