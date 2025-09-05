# pnmrotate

> Rotate a PNM image. More information: <https://netpbm.sourceforge.net/doc/pnmrotate.html>.

## Examples

### Rotate a PNM image by some angle (measured in degrees, counter-clockwise)

```bash
pnmrotate angle path/to/input.pnm > path/to/output.pnm
```

### Specify the background color exposed by rotating the input image

```bash
pnmrotate [-b|-background] color angle path/to/input.pnm > path/to/output.pnm
```

### Disable anti-aliasing, improving performance but decreasing quality

```bash
pnmrotate [-n|-noantialias] angle path/to/input.pnm > path/to/output.pnm
```
