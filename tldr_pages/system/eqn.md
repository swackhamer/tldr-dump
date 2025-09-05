# eqn

> Equation preprocessor for the groff (GNU Troff) document formatting system. See also: `troff`, `groff`. More information: <https://manned.org/eqn>.

## Examples

### Process input with equations, saving the output for future typesetting with groff to PostScript

```bash
eqn path/to/input.eqn > path/to/output.roff
```

### Typeset an input file with equations to PDF using the [me] macro package

```bash
eqn -T pdf path/to/input.eqn | groff -me -T pdf > path/to/output.pdf
```
