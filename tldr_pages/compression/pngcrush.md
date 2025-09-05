# pngcrush

> PNG compression utility. More information: <https://pmt.sourceforge.io/pngcrush>.

## Examples

### Compress a PNG file

```bash
pngcrush in.png out.png
```

### Compress all PNGs and output them to the specified directory

```bash
pngcrush -d path/to/output *.png
```

### Compress PNG file with all 114 available algorithms and pick the best result

```bash
pngcrush -rem allb -brute -reduce in.png out.png
```
