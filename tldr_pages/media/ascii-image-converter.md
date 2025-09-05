# ascii-image-converter

> Convert an image into ASCII. More information: <https://github.com/TheZoraiz/ascii-image-converter#cli-usage>.

## Examples

### Convert an image into ASCII

```bash
ascii-image-converter path/to/image|URL
```

### Colorize the output

```bash
ascii-image-converter [-C|--color] path/to/image|URL
```

### Create a tresholded image using braille (if the image is barely visible, try changing the terminal font)

```bash
ascii-image-converter [-b|--braille] path/to/image|URL
```

### Create a dithered image using braille (if the image is barely visible, try changing the terminal font)

```bash
ascii-image-converter [-b|--braille] --dither path/to/image|URL
```

### Display the image with negative colors

```bash
ascii-image-converter [-Cn|--color --negative] path/to/image|URL
```

### Use a wider range of characters to display an image (may improve image accuracy)

```bash
ascii-image-converter [-c|--complex] path/to/image|URL
```
