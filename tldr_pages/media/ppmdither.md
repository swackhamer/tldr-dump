# ppmdither

> Reduce the number of colors in an image by applying dithering. More information: <https://netpbm.sourceforge.net/doc/ppmdither.html>.

## Examples

### Read a PPM image, apply dithering and save it to a file

```bash
ppmdither path/to/image.ppm > path/to/file.ppm
```

### Specify the desired number of shades for each primary color

```bash
ppmdither [-r|-red] 2 [-g|-green] 3 [-b|-blue] 2 path/to/image.ppm > path/to/file.ppm
```

### Specify the dimensions of the dithering matrix

```bash
ppmdither [-d|-dim] 2 path/to/image.ppm > path/to/file.ppm
```
