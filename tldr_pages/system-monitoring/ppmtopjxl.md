# ppmtopjxl

> Convert a PPM image into an HP PaintJet XL PCL file. More information: <https://netpbm.sourceforge.net/doc/ppmtopjxl.html>.

## Examples

### Convert a PPM image into an PJXL file

```bash
ppmtopjxl path/to/image.ppm > path/to/output.pjxl
```

### Resize the input image

```bash
ppmtopjxl [-xsi|-xsize] 10cm [-ysi|-ysize] 5cm path/to/image.ppm > path/to/output.pjxl
```

### Shift the input image

```bash
ppmtopjxl [-xsh|-xshift] 10pt [-ysh|-yshift] 5pt path/to/image.ppm > path/to/output.pjxl
```

### Do not use the normal TIFF 4.0 compression method

```bash
ppmtopjxl [-n|-nopack] path/to/image.ppm > path/to/output.pjxl
```
