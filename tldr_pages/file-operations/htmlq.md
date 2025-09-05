# htmlq

> Use CSS selectors to extract content from HTML files. More information: <https://github.com/mgdm/htmlq>.

## Examples

### Return all elements of class `card`

```bash
cat path/to/file.html | htmlq '.card'
```

### Get the text content of the first paragraph

```bash
cat path/to/file.html | htmlq --text 'p:first-of-type'
```

### Find all the links in a page

```bash
cat path/to/file.html | htmlq --attribute href 'a'
```

### Remove all images and SVGs from a page

```bash
cat path/to/file.html | htmlq --remove-nodes 'img' --remove-nodes 'svg'
```

### Pretty print and write the output to a file

```bash
htmlq --pretty --filename path/to/input.html --output path/to/output.html
```
