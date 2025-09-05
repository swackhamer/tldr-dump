# ppmwheel

> Generate a PPM image of a color wheel. More information: <https://netpbm.sourceforge.net/doc/ppmwheel.html>.

## Examples

### Generate a color wheel of type `Ppmcirc`

```bash
ppmwheel diameter > path/to/output.ppm
```

### Generate a color wheel of type `Hue-value`

```bash
ppmwheel [-huev|-huevalue] diameter > path/to/output.ppm
```

### Generate a color wheel of type `Hue-saturation`

```bash
ppmwheel [-hues|-huesaturation] diameter > path/to/output.ppm
```
