# pgmramp

> Generate a greyscale map. More information: <https://netpbm.sourceforge.net/doc/pgmramp.html>.

## Examples

### Generate a left-to-right greyscale map

```bash
pgmramp -lr > path/to/output.pgm
```

### Generate a top-to-bottom greyscale map

```bash
pgmramp -tb > path/to/output.pgm
```

### Generate a rectangular greyscale map

```bash
pgmramp -rectangle > path/to/output.pgm
```

### Generate a elliptical greyscale map

```bash
pgmramp -ellipse path/to/image.pgm > path/to/output.pgm
```

### Generate a greyscale map from the top-left corner to the bottom-right corner

```bash
pgmramp -diagonal path/to/image.pgm > path/to/output.pgm
```
