# pdfinfo

> Portable Document Format (PDF) file information viewer. More information: <https://www.xpdfreader.com/pdfinfo-man.html>.

## Examples

### Print PDF file information

```bash
pdfinfo path/to/file.pdf
```

### Specify user password for PDF file to bypass security restrictions

```bash
pdfinfo -upw password path/to/file.pdf
```

### Specify owner password for PDF file to bypass security restrictions

```bash
pdfinfo -opw password path/to/file.pdf
```
