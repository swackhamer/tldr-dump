# xsltproc

> Transform XML with XSLT to produce output (usually HTML or XML). More information: <https://manned.org/xsltproc>.

## Examples

### Transform an XML file with a specific XSLT stylesheet

```bash
xsltproc --output path/to/output_file.html path/to/stylesheet_file.xslt path/to/file.xml
```

### Pass a value to a parameter in the stylesheet

```bash
xsltproc --output path/to/output_file.html --stringparam "name" "value" path/to/stylesheet_file.xslt path/to/xml_file.xml
```
