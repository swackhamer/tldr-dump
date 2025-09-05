# xml-select

> Select from XML documents using XPATHs. Tip: use `xml elements` to display the XPATHs of an XML document. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139652416>.

## Examples

### Select all elements matching "XPATH1" and print the value of their sub-element "XPATH2"

```bash
xml [sel|select] [-t|--template] [-m|--match] "XPATH1" [-v|--value-of] "XPATH2" path/to/input.xml|URI
```

### Match "XPATH1" and print the value of "XPATH2" as text with new-lines

```bash
xml [sel|select] [-T|--text] [-t|--template] [-m|--match] "XPATH1" [-v|--value-of] "XPATH2" [-n|--nl] path/to/input.xml|URI
```

### Count the elements of "XPATH1"

```bash
xml [sel|select] [-t|--template] [-v|--value-of] "count(XPATH1)" path/to/input.xml|URI
```

### Count all nodes in one or more XML documents

```bash
xml [sel|select] [-T|--text] [-t|--template] [-f|--inp-name] [-o|--output] " " [-v|--value-of] "count(node())" [-n|--nl] path/to/input1.xml|URI path/to/input2.xml|URI
```

### Display help

```bash
xml [sel|select] --help
```
