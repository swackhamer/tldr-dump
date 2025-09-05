# texliveonfly

> Downloads missing TeX Live packages while compiling `.tex` files. More information: <https://ctan.org/tex-archive/support/texliveonfly>.

## Examples

### Download missing packages while compiling

```bash
texliveonfly source.tex
```

### Use a specific compiler (defaults to `pdflatex`)

```bash
texliveonfly [-c|--compiler] compiler source.tex
```

### Use a custom TeX Live `bin` folder

```bash
texliveonfly --texlive_bin=path/to/texlive_bin source.tex
```
