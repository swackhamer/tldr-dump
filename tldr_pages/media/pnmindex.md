# pnmindex

> Build a visual index of multiple PNM images. See also: `pamundice`. More information: <https://netpbm.sourceforge.net/doc/pnmindex.html>.

## Examples

### Produce an image containing thumbnails of the specified images in a grid

```bash
pnmindex path/to/input1.pnm path/to/input2.pnm ... > path/to/output.pnm
```

### Specify the size of the (quadratic) thumbnails

```bash
pnmindex [-s|-size] 50 path/to/input1.pnm path/to/input2.pnm ... > path/to/output.pnm
```

### Specify the number of thumbnails per row

```bash
pnmindex [-a|-across] 10 path/to/input1.pnm path/to/input2.pnm ... > path/to/output.pnm
```

### Specify the maximum number of colors in the output

```bash
pnmindex [-c|-colors] 512 path/to/input1.pnm path/to/input2.pnm ... > path/to/output.pnm
```
