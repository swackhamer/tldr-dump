# pnmmercator

> Perform Mercator transformations on Netpbm images. See also: `pnmglobe`. More information: <https://netpbm.sourceforge.net/doc/pnmmercator.html>.

## Examples

### Convert a rectangular projection worldmap to Mercator projection

```bash
pnmmercator path/to/image.pnm > path/to/output.pnm
```

### Convert a Mercator projection worldmap to rectangular projection

```bash
pnmmercator [-i|-inverse] path/to/image.pnm > path/to/output.pnm
```
