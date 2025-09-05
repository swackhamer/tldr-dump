# ocrmypdf

> Generate a searchable PDF or PDF/A from a scanned PDF or an image of text. More information: <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>.

## Examples

### Create a new searchable PDF/A file from a scanned PDF or image file

```bash
ocrmypdf path/to/input path/to/output.pdf
```

### Skip pages of a mixed-format input PDF file that already contain text

```bash
ocrmypdf --skip-text path/to/input.pdf path/to/output.pdf
```

### Clean, de-skew, and rotate pages of a poor scan

```bash
ocrmypdf --clean --deskew --rotate-pages path/to/input.pdf path/to/output.pdf
```

### Perform lossy optimization on a PDF without performing any OCR

```bash
ocrmypdf --tesseract-timeout 0 --optimize 2 --skip-text path/to/input.pdf path/to/output.pdf
```

### Set the metadata of a searchable PDF file

```bash
ocrmypdf --title "title" --author "author" --subject "subject" --keywords "keyword; key phrase; ..." path/to/input.pdf path/to/output.pdf
```

### Display help

```bash
ocrmypdf --help
```
