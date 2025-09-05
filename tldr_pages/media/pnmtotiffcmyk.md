# pnmtotiffcmyk

> Convert a PNM image to a CMYK encoded TIFF. More information: <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>.

## Examples

### Convert a PNM image to a CMYK encoded TIFF

```bash
pnmtotiffcmyk path/to/input_file.pnm > path/to/output_file.tiff
```

### Specify the TIFF compression method

```bash
pnmtotiffcmyk -none|packbits|lzw path/to/input_file.pnm > path/to/output_file.tiff
```

### Control the fill order

```bash
pnmtotiffcmyk -msb2lsb|lsb2msb path/to/input_file.pnm > path/to/output_file.tiff
```
