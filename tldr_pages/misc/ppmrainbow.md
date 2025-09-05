# ppmrainbow

> Generate a rainbow. More information: <https://netpbm.sourceforge.net/doc/ppmrainbow.html>.

## Examples

### Generate a rainbow consisting of the specified colors

```bash
ppmrainbow color1 color2 ... > path/to/output_file.ppm
```

### Specify the size of the output in pixels

```bash
ppmrainbow [-w|-width] width [-h|-height] height color1 color2 ... > path/to/output_file.ppm
```

### End the rainbow with the last color specified, do not repeat the first color

```bash
ppmrainbow [-n|-norepeat] color1 color2 ... > path/to/output_file.ppm
```
