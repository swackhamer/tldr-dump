# xmlstarlet

> A XML/XSLT toolkit. Note: You will likely need to know XPath: <https://developer.mozilla.org/en-US/docs/Web/XPath>. More information: <https://xmlstar.sourceforge.net/docs.php>.

## Examples

### Format an XML document and print to `stdout`

```bash
xmlstarlet format path/to/file.xml
```

### XML document can also be piped from `stdin`

```bash
cat path/to/file.xml | xmlstarlet format
```

### Print all nodes that match a given XPath

```bash
xmlstarlet select --template --copy-of xpath path/to/file.xml
```

### Insert an attribute to all matching nodes, and print to `stdout` (source file is unchanged)

```bash
xmlstarlet edit --insert xpath --type attr --name attribute_name --value attribute_value path/to/file.xml
```

### Update the value of all matching nodes in place (source file is changed)

```bash
xmlstarlet edit --inplace --update xpath --value new_value file.xml
```

### Delete all matching nodes in place (source file is changed)

```bash
xmlstarlet edit --inplace --delete xpath file.xml
```

### Escape or unescape special XML characters in a given string

```bash
xmlstarlet [un]escape string
```

### List a given directory as XML (omit argument to list current directory)

```bash
xmlstarlet ls path/to/directory
```
