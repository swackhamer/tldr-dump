# pup

> HTML parsing tool. More information: <https://github.com/ericchiang/pup>.

## Examples

### Transform a raw HTML file into a cleaned, indented, and colored format

```bash
cat index.html | pup --color
```

### Filter HTML by element tag name

```bash
cat index.html | pup 'tag'
```

### Filter HTML by ID

```bash
cat index.html | pup 'div#id'
```

### Filter HTML by attribute value

```bash
cat index.html | pup 'input[type="text"]'
```

### Print all text from the filtered HTML elements and their children

```bash
cat index.html | pup 'div text{}'
```

### Print HTML as JSON

```bash
cat index.html | pup 'div json{}'
```
