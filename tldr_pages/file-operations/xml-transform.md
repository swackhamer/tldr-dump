# xml-transform

> Transform XML documents using XSLT. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139602800>.

## Examples

### Transform an XML document using an XSL stylesheet, passing one XPATH parameter and one literal string parameter

```bash
xml [tr|transform] path/to/stylesheet.xsl -p "Count='count(/xml/table/rec)'" -s Text="Count=" path/to/input.xml|URI
```

### Display help

```bash
xml [tr|transform] --help
```
