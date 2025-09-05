# latexmk

> Compile LaTeX source files into finished documents. Automatically does multiple runs when needed. More information: <https://mg.readthedocs.io/latexmk.html>.

## Examples

### Compile a DVI (Device Independent file) document from every source

```bash
latexmk
```

### Compile a DVI document from a specific source file

```bash
latexmk path/to/source.tex
```

### Compile a PDF document

```bash
latexmk -pdf path/to/source.tex
```

### Open the document in a viewer and continuously update it whenever source files change

```bash
latexmk -pvc path/to/source.tex
```

### Force the generation of a document even if there are errors

```bash
latexmk -f path/to/source.tex
```

### Clean up temporary TEX files created for a specific TEX file

```bash
latexmk -c path/to/source.tex
```

### Clean up all temporary TEX files in the current directory

```bash
latexmk -c
```
