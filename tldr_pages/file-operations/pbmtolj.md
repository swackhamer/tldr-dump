# pbmtolj

> Convert a PBM file to an HP LaserJet file. More information: <https://netpbm.sourceforge.net/doc/pbmtolj.html>.

## Examples

### Convert a PBM file to an HP LaserJet file

```bash
pbmtolj path/to/input.pbm > path/to/output.lj
```

### Compress the output file using the specified method

```bash
pbmtolj -packbits|delta|compress path/to/input.pbm > path/to/output.lj
```

### Specify the required resolution

```bash
pbmtolj [-r|-resolution] 75|100|150|300|600 path/to/input.pbm > path/to/output.lj
```
