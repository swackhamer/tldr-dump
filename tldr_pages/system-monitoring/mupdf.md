# mupdf

> A lightweight PDF, XPS, and E-book viewer. More information: <https://mupdf.readthedocs.io/en/latest/tools/mupdf-gl.html>.

## Examples

### Open a PDF on the first page

```bash
mupdf path/to/file
```

### Open a PDF on page 3

```bash
mupdf path/to/file 3
```

### Open a password secured PDF

```bash
mupdf -p password path/to/file
```

### Open a PDF with an initial zoom level, specified as DPI, of 72

```bash
mupdf -r 72 path/to/file
```

### Open a PDF with inverted color

```bash
mupdf -I path/to/file
```

### Open a PDF tinted red #FF0000 (hexadecimal color syntax RRGGBB)

```bash
mupdf -C FF0000
```

### Open a PDF without anti-aliasing (0 = off, 8 = best)

```bash
mupdf -A 0
```
