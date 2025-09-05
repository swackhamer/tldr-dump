# silicon

> Create an image of source code. More information: <https://github.com/Aloxaf/silicon>.

## Examples

### Generate an image from a specific source file

```bash
silicon path/to/source_file --output path/to/output_image
```

### Generate an image from a source file with a specific programming language syntax highlighting (e.g. `rust`, `py`, `js`, etc.)

```bash
silicon path/to/source_file --output path/to/output_image --language language|extension
```

### Generate an image from `stdin`

```bash
command | silicon --output path/to/output_image
```
