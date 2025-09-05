# pic

> Picture preprocessor for the groff (GNU Troff) document formatting system. See also: `groff`, `troff`. More information: <https://manned.org/pic>.

## Examples

### Process input with pictures, saving the output for future typesetting with groff to PostScript

```bash
pic path/to/input.pic > path/to/output.roff
```

### Typeset input with pictures to PDF using the [me] macro package

```bash
pic -T pdf path/to/input.pic | groff -me -T pdf > path/to/output.pdf
```
