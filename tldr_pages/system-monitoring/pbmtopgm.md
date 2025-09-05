# pbmtopgm

> Convert a PBM image to PGM by averaging areas surrounding individual pixels. See also: `pnmconvol`, `pamditherbw`. More information: <https://netpbm.sourceforge.net/doc/pbmtopgm.html>.

## Examples

### Convert PBM image to PGM by averaging the `w`x`h`-sized area surrounding each pixel

```bash
pbmtopgm w h path/to/image.pbm > path/to/output.pgm
```
