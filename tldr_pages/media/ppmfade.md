# ppmfade

> Generate a transition between two PPM images. More information: <https://netpbm.sourceforge.net/doc/ppmfade.html>.

## Examples

### Generate a transition between two PPM images ([f]irst and [l]ast) using the specified effect

```bash
ppmfade -f path/to/image1.ppm -l path/to/image2.ppm -mix|spread|shift|relief|oil|...
```

### Generate a transition starting with the specified image and ending in a solid black image

```bash
ppmfade -f path/to/image.ppm -mix|spread|shift|relief|oil|...
```

### Generate a transition starting with a solid black image and ending with the specified image

```bash
ppmfade -l path/to/image.ppm -mix|spread|shift|relief|oil|...
```

### Store the resulting images in files named `base.NNNN.ppm` where `NNNN` is a increasing number

```bash
ppmfade -f path/to/image1.ppm -l path/to/image2.ppm -mix|spread|shift|relief|oil|... -base base
```
