# soffice

> CLI for the powerful and free LibreOffice suite. More information: <https://help.libreoffice.org/latest/en-US/text/shared/guide/pdf_params.html>.

## Examples

### Open one or more files in read-only mode

```bash
soffice --view path/to/file1 path/to/file2 ...
```

### Display the content of one or more files

```bash
soffice --cat path/to/file1 path/to/file2 ...
```

### Print files using a specific printer

```bash
soffice --pt printer_name path/to/file1 path/to/file2 ...
```

### Convert all `.doc` files in the current directory to PDF

```bash
soffice --convert-to pdf *.doc
```
