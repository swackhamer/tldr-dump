# pnmshear

> Shear a PNM image. More information: <https://netpbm.sourceforge.net/doc/pnmshear.html>.

## Examples

### Shear a PNM image by the specified angle

```bash
pnmshear angle path/to/input.pnm > path/to/output.pnm
```

### Specify the color of the background in the sheared image

```bash
pnmshear [-b|-background] blue angle path/to/input.pnm > path/to/output.pnm
```

### Do not perform anti-aliasing

```bash
pnmshear [-n|-noantialias] angle path/to/input.pnm > path/to/output.pnm
```
