# viu

> View images on the terminal. More information: <https://github.com/atanunq/viu>.

## Examples

### Render an image or animated GIF

```bash
viu path/to/file
```

### Render an image or GIF from the internet using `curl`

```bash
curl [-s|--silent] https://example.com/image.png | viu -
```

### Render an image with a transparent background

```bash
viu [-t|--transparent] path/to/file
```

### Render an image with a specific width and height in pixels

```bash
viu [-w|--width] width [-h|--height] height path/to/file
```

### Render an image or GIF and display its file name

```bash
viu [-n|--name] path/to/file
```
