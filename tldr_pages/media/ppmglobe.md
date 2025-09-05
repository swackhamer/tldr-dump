# ppmglobe

> Generate strips of an image suitable to be glued onto a sphere. See also: `pnmmercator`. More information: <https://netpbm.sourceforge.net/doc/ppmglobe.html>.

## Examples

### Transform an image to strips that can be cut out and glues onto a sphere

```bash
ppmglobe number_of_strips path/to/image.ppm > path/to/output.ppm
```

### Use the specified color for the areas between the strips

```bash
ppmglobe [-b|-background] red number_of_strips path/to/image.ppm > path/to/output.ppm
```
