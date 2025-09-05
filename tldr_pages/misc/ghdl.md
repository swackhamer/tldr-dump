# ghdl

> Open-source simulator for the VHDL language. More information: <https://ghdl.github.io/ghdl/>.

## Examples

### Analyze a VHDL source file and produce an object file

```bash
ghdl -a filename.vhdl
```

### Elaborate a design (where `design` is the name of a configuration unit, entity unit or architecture unit)

```bash
ghdl -e design
```

### Run an elaborated design

```bash
ghdl -r design
```

### Run an elaborated design and dump output to a waveform file

```bash
ghdl -r design --wave=output.ghw
```

### Check the syntax of a VHDL source file

```bash
ghdl -s filename.vhdl
```

### Display help

```bash
ghdl --help
```
