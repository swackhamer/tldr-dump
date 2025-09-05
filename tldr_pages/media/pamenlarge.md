# pamenlarge

> Enlarge a PAM image by duplicating pixels. See also: `pbmreduce`, `pamditherbw`, `pbmpscale`. More information: <https://netpbm.sourceforge.net/doc/pamenlarge.html>.

## Examples

### Enlarge the specified image by the specified factor

```bash
pamenlarge [-s|-scale] n path/to/image.pam > path/to/output.pam
```

### Enlarge the specified image by the specified factors horizontally and vertically

```bash
pamenlarge [-x|-xscale] xn [-y|-yscale] yn path/to/image.pam > path/to/output.pam
```
