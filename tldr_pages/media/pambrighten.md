# pambrighten

> Change a PAM image's saturation and value. More information: <https://netpbm.sourceforge.net/doc/pambrighten.html>.

## Examples

### Increase the saturation of each pixel by the specified percentage

```bash
pambrighten [-s|-saturation] value_percent path/to/image.pam > path/to/output.pam
```

### Increase the value (from the HSV color space) of each pixel by the specified percentage

```bash
pambrighten [-va|-value] value_percent path/to/image.pam > path/to/output.pam
```
