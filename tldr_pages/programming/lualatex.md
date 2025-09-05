# lualatex

> An extended version of TeX using Lua to compile. More information: <https://manned.org/lualatex.1>.

## Examples

### Start `texlua` to act as a Lua interpreter

```bash
lualatex
```

### Compile a Tex file to PDF

```bash
lualatex path/to/file.tex
```

### Compile a Tex file without error interruption

```bash
lualatex -interaction nonstopmode path/to/file.tex
```

### Compile a Tex file with a specific output file name

```bash
lualatex -jobname=filename path/to/file.tex
```
