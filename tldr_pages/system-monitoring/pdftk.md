# pdftk

> PDF toolkit. More information: <https://www.pdflabs.com/docs/pdftk-man-page/>.

## Examples

### Extract pages 1-3, 5 and 6-10 from a PDF file and save them as another one

```bash
pdftk input.pdf cat 1-3 5 6-10 output output.pdf
```

### Merge (concatenate) a list of PDF files and save the result as another one

```bash
pdftk file1.pdf file2.pdf ... cat output output.pdf
```

### Split each page of a PDF file into a separate file, with a given filename output pattern

```bash
pdftk input.pdf burst output out_%d.pdf
```

### Rotate all pages by 180 degrees clockwise

```bash
pdftk input.pdf cat 1-endsouth output output.pdf
```

### Rotate third page by 90 degrees clockwise and leave others unchanged

```bash
pdftk input.pdf cat 1-2 3east 4-end output output.pdf
```
