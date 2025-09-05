# feh

> Lightweight image viewing utility. More information: <https://feh.finalrewind.org>.

## Examples

### View images locally or using a URL

```bash
feh path/to/images
```

### View images recursively

```bash
feh --recursive path/to/images
```

### View images without window borders

```bash
feh --borderless path/to/images
```

### Set the behavior when reaching the beginning or end of the image list

```bash
feh --on-last-slide hold|quit|resume path/to/images
```

### Use a specific slideshow cycle delay

```bash
feh --slideshow-delay seconds path/to/images
```

### Use a specific wallpaper mode (centered, filled, maximized, scaled or tiled)

```bash
feh --bg-center|fill|max|scale|tile path/to/image
```

### Create a montage of all images within a directory, outputting as a new image

```bash
feh --montage --thumb-height 150 --thumb-width 150 --index-info "%nn%wx%h" --output path/to/montage_image.png
```
