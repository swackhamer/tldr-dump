# magick-mogrify

> Perform operations on multiple images, such as resizing, cropping, flipping, and adding effects. Changes are applied directly to the original file. See also: `magick`. More information: <https://imagemagick.org/script/mogrify.php>.

## Examples

### Resize all JPEG images in the directory to 50% of their initial size

```bash
magick mogrify -resize 50% *.jpg
```

### Resize all images starting with `DSC` to 800x600

```bash
magick mogrify -resize 800x600 DSC*
```

### Convert all PNGs in the directory to JPEG

```bash
magick mogrify -format jpg *.png
```

### Halve the saturation of all image files in the current directory

```bash
magick mogrify -modulate 100,50 *
```

### Double the brightness of all image files in the current directory

```bash
magick mogrify -modulate 200 *
```

### Reduce file sizes of all GIF images in the current directory by reducing quality

```bash
magick mogrify -layers 'optimize' -fuzz 7% *.gif
```

### Display help

```bash
magick mogrify -help
```
