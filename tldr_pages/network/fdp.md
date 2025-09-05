# fdp

> Render an image of a `force-directed` network graph from a `graphviz` file. Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`. More information: <https://graphviz.org/doc/info/command.html>.

## Examples

### Render a PNG image with a filename based on the input filename and output format (uppercase -O)

```bash
fdp -T png -O path/to/input.gv
```

### Render a SVG image with the specified output filename (lowercase -o)

```bash
fdp -T svg -o path/to/image.svg path/to/input.gv
```

### Render the output in a specific format

```bash
fdp -T ps|pdf|svg|fig|png|gif|jpg|json|dot -O path/to/input.gv
```

### Render a `gif` image using `stdin` and `stdout`

```bash
echo "digraph {this -> that} " | fdp -T gif > path/to/image.gif
```

### Display help

```bash
fdp -?
```
