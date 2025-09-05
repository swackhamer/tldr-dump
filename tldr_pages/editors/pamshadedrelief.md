# pamshadedrelief

> Generate a shaded relief from an elevation map. See also: `pamcrater`, `ppmrelief`. More information: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

## Examples

### Generate a shaded relief image with the input image interpreted as an elevation map

```bash
pamshadedrelief < path/to/input.pam > path/to/output.pam
```

### Gamma adjust the image by the specified factor

```bash
pamshadedrelief [-g|-gamma] factor < path/to/input.pam > path/to/output.pam
```
