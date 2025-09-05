# pnmnorm

> Normalize the contrast in a PNM image. See also: `pnmhisteq`. More information: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

## Examples

### Force the brightest pixels to be white, the darkest pixels to be black and spread out the ones in between linearly

```bash
pnmnorm path/to/image.pnm > path/to/output.pnm
```

### Force the brightest pixels to be white, the darkest pixels to be black and spread out the ones in between quadratically such that pixels with a brightness of `n` become 50 % bright

```bash
pnmnorm [-midv|-midvalue] n path/to/image.pnm > path/to/output.pnm
```

### Keep the pixels' hue, only modify the brightness

```bash
pnmnorm [-k|-keephues] path/to/image.pnm > path/to/output.pnm
```

### Specify a method to calculate a pixel's brightness

```bash
pnmnorm -luminosity|colorvalue|saturation path/to/image.pnm > path/to/output.pnm
```
