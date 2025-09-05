# rasttopnm

> Convert a Sun rasterfile to a PNM file. More information: <https://netpbm.sourceforge.net/doc/rasttopnm.html>.

## Examples

### Convert a RAST image to a PNM file

```bash
rasttopnm path/to/input.rast > path/to/output.pnm
```

### Use the color map indices in the raster if they are color values

```bash
rasttopnm [-i|-index] path/to/input.rast > path/to/output.pnm
```
