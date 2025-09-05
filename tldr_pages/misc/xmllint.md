# xmllint

> XML parser and linter that supports XPath, a syntax for navigating XML trees. More information: <https://manned.org/xmllint>.

## Examples

### Return all nodes (tags) named "foo"

```bash
xmllint --xpath "//foo" source_file.xml
```

### Return the contents of the first node named "foo" as a string

```bash
xmllint --xpath "string(//foo)" source_file.xml
```

### Return the href attribute of the second anchor element in an HTML file

```bash
xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml
```

### Return human-readable (indented) XML from file

```bash
xmllint --format source_file.xml
```

### Check that an XML file meets the requirements of its DOCTYPE declaration

```bash
xmllint --valid source_file.xml
```

### Validate XML against DTD schema hosted online

```bash
xmllint --dtdvalid URL source_file.xml
```
