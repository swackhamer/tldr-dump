# ppmspread

> Displace the pixels in a PPM image by a randomized amount. More information: <https://netpbm.sourceforge.net/doc/ppmspread.html>.

## Examples

### Displace the pixels in a PPM image by a randomized amount that is at most a

```bash
ppmspread a path/to/input_file.ppm > path/to/output_file.ppm
```

### Specify a seed to a the pseudo-random number generator

```bash
ppmspread a path/to/input_file.ppm [-r|-randomseed] seed > path/to/output_file.ppm
```
