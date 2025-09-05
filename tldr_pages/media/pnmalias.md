# pnmalias

> Apply antialiasing onto a PNM image. More information: <https://netpbm.sourceforge.net/doc/pnmalias.html>.

## Examples

### Perform antialiasing on a PNM image, taking black pixels as background and white pixels as foreground

```bash
pnmalias path/to/input.pnm > path/to/output.ppm
```

### Explicitly specify the background and foreground color

```bash
pnmalias -bcolor background_color -fcolor foreground_color path/to/input.pnm > path/to/output.ppm
```

### Apply altialiasing to foreground pixels only

```bash
pnmalias [-fo|-fonly] path/to/input.pnm > path/to/output.ppm
```

### Apply antialiasing to all surrounding pixels of background pixels

```bash
pnmalias [-ba|-balias] path/to/input.pnm > path/to/output.ppm
```
