# pdfimages

> Utility for extracting images from PDFs. More information: <https://manned.org/pdfimages>.

## Examples

### Extract all images from a PDF file and save them as PNGs

```bash
pdfimages -png path/to/file.pdf filename_prefix
```

### Extract images from pages 3 to 5

```bash
pdfimages -f 3 -l 5 path/to/file.pdf filename_prefix
```

### Extract images from a PDF file and include the page number in the output filenames

```bash
pdfimages -p path/to/file.pdf filename_prefix
```

### List information about all the images in a PDF file

```bash
pdfimages -list path/to/file.pdf
```
