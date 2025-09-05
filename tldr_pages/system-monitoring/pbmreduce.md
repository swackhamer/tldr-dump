# pbmreduce

> Proportionally reduce a PBM image. See also: `pamenlarge`, `pamditherbw`. More information: <https://netpbm.sourceforge.net/doc/pbmreduce.html>.

## Examples

### Reduce the specified image by the specified factor

```bash
pbmreduce n path/to/image.pbm > path/to/output.pbm
```

### Use simple thresholding when reducing

```bash
pbmreduce [-t|-threshold] n path/to/image.pbm > path/to/output.pbm
```

### Use the specified threshold for all quantizations

```bash
pbmreduce [-va|-value] 0.6 n path/to/image.pbm > path/to/output.pbm
```
