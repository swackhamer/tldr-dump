# ppmtopj

> Convert a PPM file to an HP PaintJet file. More information: <https://netpbm.sourceforge.net/doc/ppmtopj.html>.

## Examples

### Convert a PPM file to an HP PaintJet file

```bash
ppmtopj path/to/input.ppm > path/to/output.pj
```

### Move the image in the x and y direction

```bash
ppmtopj [-x|-xpos] dx [-y|-ypos] dy path/to/input.ppm > path/to/output.pj
```

### Explicitly specify a gamma value

```bash
ppmtopj [-g|-gamma] gamma path/to/input.ppm > path/to/output.pj
```
