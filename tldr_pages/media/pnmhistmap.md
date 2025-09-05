# pnmhistmap

> Draw a histogram of a PNM image. More information: <https://netpbm.sourceforge.net/doc/pnmhistmap.html>.

## Examples

### Draw a histogram of a PNM image

```bash
pnmhistmap path/to/input.pnm > path/to/output.pnm
```

### Draw the histogram as dots instead of bars

```bash
pnmhistmap [-d|-dots] path/to/input.pnm > path/to/output.pnm
```

### Specify the range of intensity values to include

```bash
pnmhistmap [-l|-lval] minval [-rv|-rval] maxval path/to/input.pnm > path/to/output.pnm
```
