# gv2gxl

> Convert a graph from `gv` to `gxl` format. Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

## Examples

### Convert a graph from `gv` to `gxl` format

```bash
gv2gxl -o output.gxl input.gv
```

### Convert a graph using `stdin` and `stdout`

```bash
cat input.gv | gv2gxl > output.gxl
```

### Display help

```bash
gv2gxl -?
```
