# edgepaint

> Colorize edges of a graph layout to clarify crossing edges. Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. More information: <https://graphviz.org/pdf/edgepaint.1.pdf>.

## Examples

### Colorize edges of one or more graph layouts (that already have layout information) to clarify crossing edges

```bash
edgepaint path/to/layout1.gv path/to/layout2.gv ... > path/to/output.gv
```

### Colorize edges using a color scheme. (See <https://graphviz.org/doc/info/colors.html#brewer>)

```bash
edgepaint -color-scheme=accent7 path/to/layout.gv > path/to/output.gv
```

### Lay out a graph and colorize its edges, then convert to a PNG image

```bash
dot path/to/input.gv | edgepaint | dot -T png > path/to/output.png
```

### Display help

```bash
edgepaint -?
```
