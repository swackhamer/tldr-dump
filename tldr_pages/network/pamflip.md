# pamflip

> Flip or rotate a PAM or PNM image. More information: <https://netpbm.sourceforge.net/doc/pamflip.html>.

## Examples

### Rotate the input image counter-clockwise for a specific degree

```bash
pamflip [-r|-rotate]90|180|270 path/to/input.pam > path/to/output.pam
```

### Flip left for right

```bash
pamflip [-lr|-leftright] path/to/input.pam > path/to/output.pam
```

### Flip top for bottom

```bash
pamflip [-tb|-topbottom] path/to/input.pam > path/to/output.pam
```

### Flip the input image on the main diagonal

```bash
pamflip [-xy|-transpose] path/to/input.pam > path/to/output.pam
```
