# lpinfo

> List connected printers and installed drivers for the CUPS print server. More information: <https://openprinting.github.io/cups/doc/man-lpinfo.html>.

## Examples

### List all the currently connected printers

```bash
lpinfo -v
```

### List all the currently installed printer drivers

```bash
lpinfo -m
```

### Search installed printer drivers by make and model

```bash
lpinfo --make-and-model "printer_model" -m
```
