# gnuplot

> A graph plotter that outputs in several formats. More information: <https://manned.org/gnuplot>.

## Examples

### Start the interactive graph plotting shell

```bash
gnuplot
```

### Plot the graph for the specified graph definition file

```bash
gnuplot path/to/definition.plt
```

### Set the output format by executing a command before loading the definition file

```bash
gnuplot -e "set output "path/to/filename.png" size 1024,768" path/to/definition.plt
```

### Persist the graph plot preview window after gnuplot exits

```bash
gnuplot [-p|--persist] path/to/definition.plt
```
