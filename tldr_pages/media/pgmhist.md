# pgmhist

> Print a histogram of the values present in a PGM image. See also: `ppmhist`. More information: <https://netpbm.sourceforge.net/doc/pgmhist.html>.

## Examples

### Display the histogram for human reading

```bash
pgmhist path/to/image.pgm
```

### Display the median grey value

```bash
pgmhist [-me|-median] path/to/image.pgm
```

### Display four quartile grey value

```bash
pgmhist [-qua|-quartile] path/to/image.pgm
```

### Report the existence of invalid grey values

```bash
pgmhist [-f|-forensic] path/to/image.pgm
```

### Display machine-readable output

```bash
pgmhist [-ma|-machine] path/to/image.pgm
```
