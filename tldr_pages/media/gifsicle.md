# gifsicle

> Create, edit, manipulate, and get information about GIF files. More information: <https://www.lcdf.org/gifsicle>.

## Examples

### Optimize a GIF as a new file

```bash
gifsicle path/to/input.gif [-O|--optimize=]3 [-o|--output] path/to/output.gif
```

### Use batch mode (modify each given file in place) and unoptimize a GIF

```bash
gifsicle [-b|--batch] path/to/input.gif [-U|--unoptimize]
```

### Extract a frame from a GIF

```bash
gifsicle path/to/input.gif '#0' > path/to/first_frame.gif
```

### Make a GIF animation from selected GIFs

```bash
gifsicle *.gif [-d|--delay] 10 [-l|--loop] > path/to/output.gif
```

### Reduce file size using lossy compression

```bash
gifsicle [-b|--batch] path/to/input.gif [-O|--optimize=]3 --lossy=100 [-k|--colors] 16 [-f|--dither]
```

### Delete the first 10 frames and all frames after frame 20 from a GIF

```bash
gifsicle [-b|--batch] path/to/input.gif --delete '#0-9' '#20-'
```

### Modify all frames by cropping them to a rectangle, changing their scale, flipping them, and rotating them

```bash
gifsicle [-b|--batch] --crop starting_x,starting_y+rect_widthxrect_height --scale 0.25 --flip-horizontal --rotate-90|180|270 path/to/input.gif
```
