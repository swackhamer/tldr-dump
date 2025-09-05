# acyclic

> Make a directed graph acyclic by reversing some edges. Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. More information: <https://graphviz.org/pdf/acyclic.1.pdf>.

## Examples

### Make a directed graph acyclic by reversing some edges

```bash
acyclic path/to/input.gv > path/to/output.gv
```

### Print if a graph is acyclic, has a cycle, or is undirected, producing no output graph

```bash
acyclic -v -n path/to/input.gv
```

### Display help

```bash
acyclic -?
```
