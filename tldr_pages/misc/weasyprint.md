# weasyprint

> Render HTML to PDF or PNG. More information: <https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#command-line-api>.

## Examples

### Render an HTML file to PDF

```bash
weasyprint path/to/input.html path/to/output.pdf
```

### Render an HTML file to PNG, including an additional user stylesheet

```bash
weasyprint path/to/input.html path/to/output.png --stylesheet path/to/stylesheet.css
```

### Output additional debugging information when rendering

```bash
weasyprint path/to/input.html path/to/output.pdf --verbose
```

### Specify a custom resolution when outputting to PNG

```bash
weasyprint path/to/input.html path/to/output.png --resolution 300
```

### Specify a base URL for relative URLs in the input HTML file

```bash
weasyprint path/to/input.html path/to/output.png --base-url url_or_filename
```
