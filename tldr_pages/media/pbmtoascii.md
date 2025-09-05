# pbmtoascii

> Convert a PBM image to ASCII graphics. See also: `ppmtoascii`, `asciitopgm`, `ppmtoterm`. More information: <https://netpbm.sourceforge.net/doc/pbmtoascii.html>.

## Examples

### Read a PBM file as input and produce an ASCII output

```bash
pbmtoascii path/to/input_file.pbm
```

### Read a PBM file as input and save an ASCII output into a file

```bash
pbmtoascii path/to/input_file.pbm > path/to/output_file
```

### Read a PBM file as input while setting the pixel mapping (defaults to 1x2)

```bash
pbmtoascii -1x2|2x4 path/to/input_file.pbm
```

### Display version

```bash
pbmtoascii [-v|-version]
```
