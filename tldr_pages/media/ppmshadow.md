# ppmshadow

> Add simulated shadows to a PPM image. More information: <https://netpbm.sourceforge.net/doc/ppmshadow.html>.

## Examples

### Add simulated shadows to a PPM image

```bash
ppmshadow path/to/input_file.ppm > path/to/output_file.ppm
```

### [b]lur the image by the specified number of pixels

```bash
ppmshadow -b n path/to/input_file.ppm > path/to/output_file.ppm
```

### Specify the displacement of the simulated light source to the left and the top of the image

```bash
ppmshadow -x left_offset -y top_offset path/to/input_file.ppm > path/to/output_file.ppm
```
