# typst

> Compile a Typst file to PDF. Note: Specifying the output location is optional. More information: <https://github.com/typst/typst>.

## Examples

### Initialize a new Typst project in a given directory using a template (e.g., `@preview/charged-ieee`)

```bash
typst init "template" path/to/directory
```

### Compile a Typst file

```bash
typst compile path/to/source.typ path/to/output.pdf
```

### Watch a Typst file and recompile on changes

```bash
typst watch path/to/source.typ path/to/output.pdf
```

### List all discoverable fonts in the system and the given directory

```bash
typst --font-path path/to/fonts_directory fonts
```
