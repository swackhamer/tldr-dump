# mdatopbm

> Convert a Microdesign MDA file to a PBM image. See also: `pbmtomda`. More information: <https://netpbm.sourceforge.net/doc/mdatopbm.html>.

## Examples

### Convert a MDA file to a PBM image

```bash
mdatopbm path/to/image.mda > path/to/output.pbm
```

### Invert the colors in the input image

```bash
mdatopbm -i path/to/image.mda > path/to/output.pbm
```

### Double the input image's height

```bash
mdatopbm -d path/to/image.mda > path/to/output.pbm
```
