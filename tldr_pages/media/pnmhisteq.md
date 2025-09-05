# pnmhisteq

> Histogram-equalize a PNM image. More information: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

## Examples

### Increase the contrast of a PNM image using histogram equalization

```bash
pnmhisteq path/to/input.pnm > path/to/output.pnm
```

### Only modify grey pixels

```bash
pnmhisteq [-g|-grey] path/to/input.pnm > path/to/output.pnm
```

### Do not include black or white pixels in the histogram equalization

```bash
pnmhisteq -noblack|white path/to/input.pnm > path/to/output.pnm
```
