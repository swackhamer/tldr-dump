# ppmtomitsu

> Convert a PPM image to a Mitsubishi S340-10 file. More information: <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>.

## Examples

### Convert a PPM image to a MITSU file

```bash
ppmtomitsu path/to/file.ppm > path/to/file.mitsu
```

### Enlarge the image by the specified factor, use the specified sharpness and produce `n` copies

```bash
ppmtomitsu [-e|-enlarge] 1|2|3 [-s|-sharpness] 1|2|3|4 [-c|-copy] n path/to/file.ppm > path/to/file.mitsu
```

### Use the given medium for the printing process

```bash
ppmtomitsu [-m|-media] A|A4|AS|A4S path/to/file.ppm > path/to/file.mitsu
```
