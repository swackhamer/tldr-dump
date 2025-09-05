# sips

> Apple Scriptable Image Processing System. Raster/Query images and ColorSync ICC Profiles. More information: <https://keith.github.io/xcode-man-pages/sips.1.html>.

## Examples

### Specify an output directory so that originals do not get modified

```bash
sips --out path/to/out_dir
```

### Resample image at specified size, Image aspect ratio may be altered

```bash
sips --resampleHeightWidth 1920 300 image_file.ext
```

### Resample image so height and width aren't greater than specified size (notice the capital Z)

```bash
sips --resampleHeightWidthMax 1920 300 image_file.ext
```

### Resample all images in a directory to fit a width of 960px (honoring aspect ratio)

```bash
sips --resampleWidth 960 path/to/images
```

### Convert an image from CMYK to RGB

```bash
sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" path/to/image.ext path/to/out_dir
```

### Remove ColorSync ICC profile from an image

```bash
sips --deleteProperty profile --deleteColorManagementProperties path/to/image_file.ext
```
