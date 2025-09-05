# xpdf

> Portable Document Format (PDF) file viewer. More information: <https://www.xpdfreader.com/xpdf-man.html>.

## Examples

### Open a PDF file

```bash
xpdf path/to/file.pdf
```

### Open a specific page in a PDF file

```bash
xpdf path/to/file.pdf :page_number
```

### Open a compressed PDF file

```bash
xpdf path/to/file.pdf.tar
```

### Open a PDF file in fullscreen mode

```bash
xpdf -fullscreen path/to/file.pdf
```

### Specify the initial zoom

```bash
xpdf -z 75% path/to/file.pdf
```

### Specify the initial zoom at page width or full page

```bash
xpdf -z page|width path/to/file.pdf
```
