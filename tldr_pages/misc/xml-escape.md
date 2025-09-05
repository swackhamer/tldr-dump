# xml-escape

> Escape special XML characters, e.g. `<a1>` → `&lt;a1&gt;`. More information: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960>.

## Examples

### Escape special XML characters in a string

```bash
xml [esc|escape] "<a1>"
```

### Escape special XML characters from `stdin`

```bash
echo "<a1>" | xml [esc|escape]
```

### Display help

```bash
xml [esc|escape] --help
```
