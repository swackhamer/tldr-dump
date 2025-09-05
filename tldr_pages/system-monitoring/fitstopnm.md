# fitstopnm

> Convert a Flexible Image Transport System (FITS) file to a PNM image. See also: `pamtofits`. More information: <https://netpbm.sourceforge.net/doc/fitstopnm.html>.

## Examples

### Convert a FITS file to a PNM image

```bash
fitstopnm path/to/file.fits > path/to/output.pnm
```

### Convert the image on the specified position of the third axis in the FITS file

```bash
fitstopnm [-i|-image] z_position path/to/file.fits > path/to/output.pnm
```
