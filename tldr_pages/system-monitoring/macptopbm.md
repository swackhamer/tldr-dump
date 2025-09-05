# macptopbm

> Read a MacPaint file as input and produce a PBM image as output. See also: `pbmtomacp`. More information: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

## Examples

### Convert a MacPaint file into a PGM image

```bash
macptopbm path/to/file.macp > path/to/output.pbm
```

### Skip over `n` bytes when reading the file

```bash
macptopbm [-e|-extraskip] n > path/to/output.pbm
```

### Suppress all informational messages

```bash
macptopbm [-q|-quiet] > path/to/output.pbm
```

### Display version

```bash
macptopbm [-v|-version]
```
