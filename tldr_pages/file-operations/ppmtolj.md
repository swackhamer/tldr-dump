# ppmtolj

> Convert a PPM file to an HP LaserJet PCL 5 Color file. More information: <https://netpbm.sourceforge.net/doc/ppmtolj.html>.

## Examples

### Convert a PPM file to an HP LaserJet PCL 5 Color file

```bash
ppmtolj path/to/input.ppm > path/to/output.lj
```

### Apply a gamma correction using the specified gamma value

```bash
ppmtolj [-g|-gamma] gamma path/to/input.ppm > path/to/output.lj
```

### Specify the required resolution

```bash
ppmtolj [-r|-resolution] 75|100|150|300|600 path/to/input.ppm > path/to/output.lj
```
