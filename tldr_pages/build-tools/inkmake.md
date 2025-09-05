# inkmake

> GNU Makefile-style SVG exporting using Inkscape's backend. More information: <https://github.com/wader/inkmake>.

## Examples

### Export an SVG file executing the specified Inkfile

```bash
inkmake path/to/Inkfile
```

### Execute an Inkfile and show detailed information

```bash
inkmake --verbose path/to/Inkfile
```

### Execute an Inkfile, specifying SVG input file(s) and an output file

```bash
inkmake --svg path/to/file.svg --out path/to/output_image path/to/Inkfile
```

### Use a custom Inkscape binary as the backend

```bash
inkmake --inkscape /Applications/Inkscape.app/Contents/Resources/bin/inkscape path/to/Inkfile
```

### Display help

```bash
inkmake --help
```
