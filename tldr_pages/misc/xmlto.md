# xmlto

> Apply an XSL stylesheet to an XML document. More information: <https://manned.org/xmlto>.

## Examples

### Convert a DocBook XML document to PDF format

```bash
xmlto pdf document.xml
```

### Convert a DocBook XML document to HTML format and store the resulting files in a separate directory

```bash
xmlto -o path/to/html_files html document.xml
```

### Convert a DocBook XML document to a single HTML file

```bash
xmlto html-nochunks document.xml
```

### Specify a stylesheet to use while converting a DocBook XML document

```bash
xmlto -x stylesheet.xsl output_format document.xml
```
