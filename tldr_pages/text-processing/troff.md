# troff

> Typesetting processor for the groff (GNU Troff) document formatting system. See also: `groff`. More information: <https://manned.org/troff>.

## Examples

### Format output for a PostScript printer, saving the output to a file

```bash
troff path/to/input.roff | grops > path/to/output.ps
```

### Format output for a PostScript printer using the me macro package, saving the output to a file

```bash
troff -me path/to/input.roff | grops > path/to/output.ps
```

### Format output as ASCII text using the man macro package

```bash
troff -T ascii -man path/to/input.roff | grotty
```

### Format output as a pdf file, saving the output to a file

```bash
troff -T pdf path/to/input.roff | gropdf > path/to/output.pdf
```
