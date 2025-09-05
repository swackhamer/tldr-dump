# pamtouil

> Convert a PNM or PAM file into a Motif UIL icon file. More information: <https://netpbm.sourceforge.net/doc/pamtouil.html>.

## Examples

### Convert a PNM or PAM file into a Motif UIL icon file

```bash
pamtouil path/to/input.pnm|pam > path/to/output.uil
```

### Specify a prefix string to be printed in the output UIL file

```bash
pamtouil [-n|-name] uilname path/to/input.pnm|pam > path/to/output.uil
```
