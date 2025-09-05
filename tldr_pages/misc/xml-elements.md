# xml-elements

> Extract elements and display the structure of an XML document. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139665568>.

## Examples

### Extract elements from an XML document (producing XPATH expressions)

```bash
xml [el|elements] path/to/input.xml|URI > path/to/elements.xpath
```

### Extract elements and their attributes from an XML document

```bash
xml [el|elements] -a path/to/input.xml|URI > path/to/elements.xpath
```

### Extract elements and their attributes and values from an XML document

```bash
xml [el|elements] -v path/to/input.xml|URI > path/to/elements.xpath
```

### Print sorted unique elements from an XML document to see its structure

```bash
xml [el|elements] -u path/to/input.xml|URI
```

### Print sorted unique elements from an XML document up to a depth of 3

```bash
xml [el|elements] -d3 path/to/input.xml|URI
```

### Display help

```bash
xml [el|elements] --help
```
