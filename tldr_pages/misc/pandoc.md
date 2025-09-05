# pandoc

> Convert documents between various formats. More information: <https://pandoc.org/MANUAL.html>.

## Examples

### Convert a Markdown file to PDF using `pdflatex` (the formats are determined by file extensions)

```bash
pandoc path/to/input.md [-o|--output] path/to/output.pdf
```

### Convert a Markdown file to PDF using the specified PDF engine

```bash
pandoc path/to/input.md --pdf-engine tectonic|weasyprint|typst|... [-o|--output] path/to/output.pdf
```

### Convert to a standalone file with the appropriate headers/footers (for LaTeX, HTML, etc.)

```bash
pandoc path/to/input.md [-s|--standalone] [-o|--output] path/to/output.html
```

### Manually specify formats (overriding automatic format detection using the filename extension, or when there is no extension)

```bash
pandoc [-f|--from] docx|... path/to/input [-t|--to] pdf|... [-o|--output] path/to/output
```

### Transform a document using a Lua script (see <https://pandoc.org/lua-filters.html> for more information)

```bash
pandoc path/to/input [-L|--lua-filter] path/to/filter.lua [-o|--output] path/to/output
```

### List all supported input formats

```bash
pandoc --list-input-formats
```

### List all supported output formats

```bash
pandoc --list-output-formats
```
