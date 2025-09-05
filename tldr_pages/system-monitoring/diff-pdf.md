# diff-pdf

> Compare two PDFs. More information: <https://github.com/vslavik/diff-pdf>.

## Examples

### Compare PDFs, indicating changes using return codes (`0` = no difference, `1` = PDFs differ)

```bash
diff-pdf path/to/a.pdf path/to/b.pdf
```

### Compare PDFs, outputting a PDF with visually highlighted differences

```bash
diff-pdf --output-diff=path/to/diff.pdf path/to/a.pdf path/to/b.pdf
```

### Compare PDFs, viewing differences in a simple GUI

```bash
diff-pdf --view path/to/a.pdf path/to/b.pdf
```
