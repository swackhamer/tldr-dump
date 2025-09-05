# xml-format

> Format an XML document. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139569312>.

## Examples

### Format an XML document, indenting with tabs

```bash
xml [fo|format] [-t|--indent-tab] path/to/input.xml|URI > path/to/output.xml
```

### Format an HTML document, indenting with 4 spaces

```bash
xml [fo|format] [-H|--html] [-s|--indent-spaces] 4 path/to/input.html|URI > path/to/output.html
```

### Recover parsable parts of a malformed XML document, without indenting

```bash
xml [fo|format] [-R|--recover] [-n|--noindent] path/to/malformed.xml|URI > path/to/recovered.xml
```

### Format an XML document from `stdin`, removing the `DOCTYPE` declaration

```bash
cat path\to\input.xml | xml [fo|format] [-D|--dropdtd] > path/to/output.xml
```

### Format an XML document, omitting the XML declaration

```bash
xml [fo|format] [-o|--omit-decl] path\to\input.xml|URI > path/to/output.xml
```

### Display help

```bash
xml [fo|format] --help
```
