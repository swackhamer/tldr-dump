# latexdiff

> Determine differences between two LaTeX files. More information: <https://ctan.org/pkg/latexdiff>.

## Examples

### Determine changes between different versions of a LaTeX file (the resulting LaTeX file can be compiled to show differences underlined)

```bash
latexdiff old.tex new.tex > diff.tex
```

### Determine changes between different versions of a LaTeX file by highlighting differences in boldface

```bash
latexdiff --type=BOLD old.tex new.tex > diff.tex
```

### Determine changes between different versions of a LaTeX file, and display minor changes in equations with both added and deleted graphics

```bash
latexdiff --math-markup=fine --graphics-markup=both old.tex new.tex > diff.tex
```
