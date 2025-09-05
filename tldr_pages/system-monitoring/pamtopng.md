# pamtopng

> Convert a PAM image to PNG. See also: `pnmtopng`, `pngtopam`. More information: <https://netpbm.sourceforge.net/doc/pamtopng.html>.

## Examples

### Convert the specified PAM image to PNG

```bash
pamtopng path/to/image.pam > path/to/output.png
```

### Mark the specified color as transparent in the output image

```bash
pamtopng [-t|-transparent] color path/to/image.pam > path/to/output.png
```

### Include the text in the specified file as tEXt chunks in the output

```bash
pamtopng [-te|-text] path/to/file.txt path/to/image.pam > path/to/output.png
```

### Cause the output file to be interlaced in Adam7 format

```bash
pamtopng [-in|-interlace] path/to/image.pam > path/to/output.png
```
