# ppmtoilbm

> Convert a PPM image to an ILBM file. More information: <https://netpbm.sourceforge.net/doc/ppmtoilbm.html>.

## Examples

### Convert a PPM image to an ILBM file

```bash
ppmtoilbm path/to/file.ppm > path/to/file.ilbm
```

### Write a maximum of n planes to the ILBM file and produce a HAM/24bit/direct color file if this number is exceeded

```bash
ppmtoilbm [-mp|-maxplanes] n -hamif|24if|dcif path/to/file.ppm > path/to/file.ilbm
```

### Produce a ILBM file with exactly n planes

```bash
ppmtoilbm [-fp|-fixplanes] n path/to/file.ppm > path/to/file.ilbm
```

### Select the compression method to be used

```bash
ppmtoilbm -compress|nocompress|savemem path/to/file.ppm > path/to/file.ilbm
```
