# gxl2gv

> Convert a graph from `gxl` to `gv` format. Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

## Examples

### Convert a graph from `gxl` to `gv` format

```bash
gxl2gv -o output.gv input.gxl
```

### Convert a graph using `stdin` and `stdout`

```bash
cat input.gxl | gxl2gv > output.gv
```

### Display help

```bash
gxl2gv -?
```
