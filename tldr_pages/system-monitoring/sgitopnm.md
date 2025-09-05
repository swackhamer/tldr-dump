# sgitopnm

> Convert an SGI file to a PNM file. More information: <https://netpbm.sourceforge.net/doc/sgitopnm.html>.

## Examples

### Convert an SGI image to a PNM file

```bash
sgitopnm path/to/input.sgi > path/to/output.pnm
```

### Display information about the SGI file

```bash
sgitopnm [-verb|-verbose] path/to/input.sgi > path/to/output.pnm
```

### Extract channel n of the SGI file

```bash
sgitopnm [-c|-channel] n path/to/input.sgi > path/to/output.pnm
```
