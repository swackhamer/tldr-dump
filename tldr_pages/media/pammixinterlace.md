# pammixinterlace

> Merge each row in an image with its two neighbours. See also: `pamdeinterlace`. More information: <https://netpbm.sourceforge.net/doc/pammixinterlace.html>.

## Examples

### Merge each row in an image with its two neighbours

```bash
pammixinterlace path/to/image.ppm > path/to/output.ppm
```

### Use the specified filtering mechanism

```bash
pammixinterlace [-f|-filter] linear|fir|ffmpeg path/to/image.ppm > path/to/output.ppm
```

### Turn on adaptive filtering mode, i.e., only modify pixels that are obviously part of a comb pattern

```bash
pammixinterlace [-a|-adaptive] path/to/image.ppm > path/to/output.ppm
```
