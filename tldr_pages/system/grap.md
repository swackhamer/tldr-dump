# grap

> A charting preprocessor for the groff (GNU Troff) document formatting system. See also: `pic`, `groff`. More information: <https://manned.org/grap>.

## Examples

### Process a `grap` file and save the output file for future processing with `pic` and `groff`

```bash
grap path/to/input.grap > path/to/output.pic
```

### Typeset a `grap` file to PDF using the [me] macro package, saving the output to a file

```bash
grap path/to/input.grap | pic -T pdf | groff -me -T pdf > path/to/output.pdf
```
