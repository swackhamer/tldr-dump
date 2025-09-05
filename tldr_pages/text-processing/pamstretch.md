# pamstretch

> Scale up a PAM image by interpolating between pixels. See also: `pamstretch-gen`, `pamenlarge`, `pamscale`. More information: <https://netpbm.sourceforge.net/doc/pamstretch.html>.

## Examples

### Scale up a PAM image by an integer factor

```bash
pamstretch n path/to/image.pam > path/to/output.pam
```

### Scale up a PAM image by the specified factors in the horizontal and vertical directions

```bash
pamstretch [-x|-xscale] xn [-y|-yscale] yn path/to/image.pam > path/to/output.pam
```
