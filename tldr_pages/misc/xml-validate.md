# xml-validate

> Validate XML documents. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139576400>.

## Examples

### Validate one or more XML documents for well-formedness only

```bash
xml [val|validate] path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...
```

### Validate one or more XML documents against a Document Type Definition (DTD)

```bash
xml [val|validate] [-d|--dtd] path/to/schema.dtd path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...
```

### Validate one or more XML documents against an XML Schema Definition (XSD)

```bash
xml [val|validate] [-s|--xsd] path/to/schema.xsd path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...
```

### Validate one or more XML documents against a Relax NG schema (RNG)

```bash
xml [val|validate] [-r|--relaxng] path/to/schema.rng path/to/input1.xml|URI1 path/to/input2.xml|URI2 ...
```

### Display help

```bash
xml [val|validate] --help
```
