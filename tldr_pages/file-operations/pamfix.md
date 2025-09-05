# pamfix

> Fix errors in PAM, PBM, PGM and PPM files. See also: `pamfile`, `pamvalidate`. More information: <https://netpbm.sourceforge.net/doc/pamfix.html>.

## Examples

### Fix a Netpbm file that is missing its last part

```bash
pamfix [-t|-truncate] path/to/corrupted.ext > path/to/output.ext
```

### Fix a Netpbm file where pixel values exceed the image's `maxval` by lowering the offending pixels' values

```bash
pamfix [-cl|-clip] path/to/corrupted.ext > path/to/output.ext
```

### Fix a Netpbm file where pixel values exceed the image's `maxval` by increasing it

```bash
pamfix [-ch|-changemaxval] path/to/corrupted.pam|pbm|pgm|ppm > path/to/output.pam|pbm|pgm|ppm
```
