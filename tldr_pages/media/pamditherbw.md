# pamditherbw

> Apply dithering to a greyscale image, i.e. turn it into a pattern of black and white pixels that look the same as the original greyscale. See also: `pbmreduce`. More information: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

## Examples

### Read a PGM image, apply dithering and save it to a file

```bash
pamditherbw path/to/image.pgm > path/to/file.pgm
```

### Use the specified quantization method

```bash
pamditherbw -floyd|fs|atkinson|threshold|hilbert|... path/to/image.pgm > path/to/file.pgm
```

### Use the atkinson quantization method and the specified seed for a pseudo-random number generator

```bash
pamditherbw [-a|-atkinson] [-r|-randomseed] 1337 path/to/image.pgm > path/to/file.pgm
```

### Specify the thresholding value for quantization methods that perform some sort of thresholding

```bash
pamditherbw -fs|atkinson|thresholding [-va|-value] 0.3 path/to/image.pgm > path/to/file.pgm
```
