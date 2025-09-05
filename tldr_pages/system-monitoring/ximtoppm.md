# ximtoppm

> Convert a XIM file to a PPM image. More information: <https://netpbm.sourceforge.net/doc/ximtoppm.html>.

## Examples

### Convert an XIM image to a PPM image

```bash
ximtoppm path/to/input_file.xim > path/to/output_file.ppm
```

### Store the transparency mask of the input image in the specified file

```bash
ximtoppm [-a|-alphaout] path/to/alpha_file.pbm path/to/input_file.xim > path/to/output_file.ppm
```
