# pamdeinterlace

> Remove every other row in a Netpbm image. See also: `pammixinterlace`. More information: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>.

## Examples

### Produce an image consisting of the input's even-numbered rows

```bash
pamdeinterlace path/to/image.ppm > path/to/output.ppm
```

### Produce an image consisting of the input's odd-numbered rows

```bash
pamdeinterlace [-takeo|-takeodd] path/to/image.ppm > path/to/output.ppm
```
