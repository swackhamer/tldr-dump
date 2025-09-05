# pdffonts

> Portable Document Format (PDF) file fonts information viewer. More information: <https://www.xpdfreader.com/pdffonts-man.html>.

## Examples

### Print PDF file fonts information

```bash
pdffonts path/to/file.pdf
```

### Specify user password for PDF file to bypass security restrictions

```bash
pdffonts -upw password path/to/file.pdf
```

### Specify owner password for PDF file to bypass security restrictions

```bash
pdffonts -opw password path/to/file.pdf
```

### Print additional information on location of the font that will be used when the PDF file is rasterized

```bash
pdffonts -loc path/to/file.pdf
```

### Print additional information on location of the font that will be used when the PDF file is converted to PostScript

```bash
pdffonts -locPS path/to/file.pdf
```
