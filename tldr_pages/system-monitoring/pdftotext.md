# pdftotext

> Convert PDF files to plain text format. More information: <https://www.xpdfreader.com/pdftotext-man.html>.

## Examples

### Convert `filename.pdf` to plain text and print it to `stdout`

```bash
pdftotext filename.pdf -
```

### Convert `filename.pdf` to plain text and save it as `filename.txt`

```bash
pdftotext filename.pdf
```

### Convert `filename.pdf` to plain text and preserve the layout

```bash
pdftotext -layout filename.pdf
```

### Convert `input.pdf` to plain text and save it as `output.txt`

```bash
pdftotext input.pdf output.txt
```

### Convert pages 2, 3 and 4 of `input.pdf` to plain text and save them as `output.txt`

```bash
pdftotext -f 2 -l 4 input.pdf output.txt
```
