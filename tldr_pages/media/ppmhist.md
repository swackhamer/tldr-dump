# ppmhist

> Print a histogram of the colors present in a PPM image. See also: `pgmhist`. More information: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

## Examples

### Generate the histogram for human reading

```bash
ppmhist [-nom|-nomap] path/to/image.ppm
```

### Generate a PPM file of the colormap for the image, with the color histogram as comments

```bash
ppmhist [-m|-map] path/to/image.ppm
```

### Display version

```bash
ppmhist [-v|-version]
```
