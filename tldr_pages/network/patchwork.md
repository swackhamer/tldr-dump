# patchwork

> Render an image of a `squareified treemap` network graph from a `graphviz` file. Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`. More information: <https://graphviz.org/doc/info/command.html>.

## Examples

### Render a PNG image with a filename based on the input filename and output format (uppercase -O)

```bash
patchwork -T png -O path/to/input.gv
```

### Render a SVG image with the specified output filename (lowercase -o)

```bash
patchwork -T svg -o path/to/image.svg path/to/input.gv
```

### Render the output in PS, PDF, SVG, Fig, PNG, GIF, JPEG, JSON, or DOT format

```bash
patchwork -T format -O path/to/input.gv
```

### Render a `gif` image using `stdin` and `stdout`

```bash
echo "digraph {this -> that} " | patchwork -T gif > path/to/image.gif
```

### Display help

```bash
patchwork -?
```
