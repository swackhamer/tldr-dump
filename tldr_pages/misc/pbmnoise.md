# pbmnoise

> Generate white noise. More information: <https://netpbm.sourceforge.net/doc/pbmnoise.html>.

## Examples

### Generate a PGM image containing white noise

```bash
pbmnoise width height > path/to/output.pbm
```

### Specify the seed for the pseudo-random number generator

```bash
pbmnoise width height -randomseed value > path/to/output.pbm
```

### Specify the desired rate of white to black pixels

```bash
pbmnoise width height -ratio 1/3 > path/to/output.pbm
```
