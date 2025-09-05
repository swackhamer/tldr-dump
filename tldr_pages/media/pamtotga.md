# pamtotga

> Convert a Netpbm image to a TrueVision Targa file. More information: <https://netpbm.sourceforge.net/doc/pamtotga.html>.

## Examples

### Convert a Netpbm image to a TrueVision Targa file

```bash
pamtotga path/to/file.pam > path/to/output.tga
```

### Specify the color map of the output image

```bash
pamtotga -cmap|cmap16|mono|rgb path/to/file.pam > path/to/output.tga
```

### Display version

```bash
pamtotga [-v|-version]
```
