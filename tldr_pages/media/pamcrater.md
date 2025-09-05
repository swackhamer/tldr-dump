# pamcrater

> Create a PAM image of cratered terrain. See also: `pamshadedrelief`, `ppmrelief`. More information: <https://netpbm.sourceforge.net/doc/pamcrater.html>.

## Examples

### Create an image of cratered terrain with the specified dimensions

```bash
pamcrater [-h|-height] height [-w|-width] width > path/to/output.pam
```

### Create an image containing the specified number of craters

```bash
pamcrater [-n|-number] n_craters > path/to/output.pam
```
