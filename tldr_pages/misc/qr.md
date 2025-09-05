# qr

> Generate QR codes in the terminal with ANSI VT-100 escape codes. More information: <https://manned.org/qr>.

## Examples

### Generate a QR code

```bash
qr "data"
```

### Specify the error correction level (defaults to `M`)

```bash
qr --error-correction L|M|Q|H "data"
```

### Generate a QR code from the output of another command

```bash
command | qr
```

### Save the QR code as a PNG image

```bash
qr "data" > path/to/file.png
```
