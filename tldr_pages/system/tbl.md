# tbl

> Table preprocessor for the groff (GNU Troff) document formatting system. See also: `groff`, `troff`. More information: <https://manned.org/tbl>.

## Examples

### Process input with tables, saving the output for future typesetting with groff to PostScript

```bash
tbl path/to/input_file > path/to/output.roff
```

### Typeset input with tables to PDF using the [me] macro package

```bash
tbl -T pdf path/to/input.tbl | groff -me -T pdf > path/to/output.pdf
```
