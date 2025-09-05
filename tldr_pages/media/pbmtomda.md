# pbmtomda

> Convert a PBM image to a Microdesign MDA file. See also: `mdatopbm`. More information: <https://netpbm.sourceforge.net/doc/pbmtomda.html>.

## Examples

### Convert a PBM image to a MDA file

```bash
pbmtomda path/to/image.pbm > path/to/output.mda
```

### Invert the colors in the input image

```bash
pbmtomda -i path/to/image.pbm > path/to/output.mda
```

### Halve the input image's height

```bash
pbmtomda -d path/to/image.pbm > path/to/output.mda
```
