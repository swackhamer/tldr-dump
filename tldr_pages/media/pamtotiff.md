# pamtotiff

> Convert a PAM image to a TIFF file. More information: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

## Examples

### Convert a PAM image to a TIFF image

```bash
pamtotiff path/to/input_file.pam > path/to/output_file.tiff
```

### Explicitly specify a compression method for the output file

```bash
pamtotiff -none|packbits|lzw|g3|g4|flate|adobeflate path/to/input_file.pam > path/to/output_file.tiff
```

### Always produce a color TIFF image, even if the input image is greyscale

```bash
pamtotiff [-c|-color] path/to/input_file.pam > path/to/output_file.tiff
```
