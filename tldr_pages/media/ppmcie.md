# ppmcie

> Draw a CIE color chart as a PPM image. More information: <https://netpbm.sourceforge.net/doc/ppmcie.html>.

## Examples

### Draw a CIE color chart using the REC709 color system as a PPM image

```bash
ppmcie > path/to/output.ppm
```

### Specify the color system to be used

```bash
ppmcie -cie|ebu|hdtv|ntsc|smpte > path/to/output.ppm
```

### Specify the location of the individual illuminants

```bash
ppmcie -red|green|blue xpos ypos > path/to/output.ppm
```

### Do not dim the area outside the Maxwell triangle

```bash
ppmcie [-f|-full] > path/to/output.ppm
```
