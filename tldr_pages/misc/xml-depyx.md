# xml-depyx

> Convert a PYX (ESIS - ISO 8879) document to XML format. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

## Examples

### Convert a PYX (ESIS - ISO 8879) document to XML format

```bash
xml [p2x|depyx] path/to/input.pyx|URI > path/to/output.xml
```

### Convert a PYX document from `stdin` to XML format

```bash
cat path/to/input.pyx | xml [p2x|depyx] > path/to/output.xml
```

### Display help

```bash
xml [p2x|depyx] --help
```
