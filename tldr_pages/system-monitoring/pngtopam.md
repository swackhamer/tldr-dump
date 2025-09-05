# pngtopam

> Convert a PNG image to a Netpbm image. See also: `pamtopng`. More information: <https://netpbm.sourceforge.net/doc/pngtopam.html>.

## Examples

### Convert the specified PNG image to a Netpbm image

```bash
pngtopam path/to/image.png > path/to/output.pam
```

### Create an output image that includes both the main image and transparency mask of the input image

```bash
pngtopam -alphapam path/to/image.png > path/to/output.pam
```

### Replace transparent pixels by the specified color

```bash
pngtopam [-m|-mix] [-ba|-background] color path/to/image.png > path/to/output.pam
```

### Write tEXt chunks found in the input image to the specified text file

```bash
pngtopam [-te|-text] path/to/file.txt path/to/image.png > path/to/output.pam
```
