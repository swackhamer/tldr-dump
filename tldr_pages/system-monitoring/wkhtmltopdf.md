# wkhtmltopdf

> Convert HTML documents or web pages into PDF files. More information: <https://wkhtmltopdf.org/usage/wkhtmltopdf.txt>.

## Examples

### Convert a HTML document into PDF

```bash
wkhtmltopdf input.html output.pdf
```

### Specify the PDF page size (please see `PaperSize` of `QPrinter` for supported sizes)

```bash
wkhtmltopdf --page-size A4 input.html output.pdf
```

### Set the PDF page margins

```bash
wkhtmltopdf --margin-top|bottom|left|right 10mm input.html output.pdf
```

### Set the PDF page orientation

```bash
wkhtmltopdf --orientation Landscape|Portrait input.html output.pdf
```

### Generate a greyscale version of the PDF document

```bash
wkhtmltopdf --grayscale input.html output.pdf
```
