# pygmentize

> Python-based syntax highlighter. More information: <https://pygments.org/docs/cmdline/>.

## Examples

### Highlight file syntax and print to `stdout` (language is inferred from the file extension)

```bash
pygmentize file.py
```

### Explicitly set the language for syntax highlighting

```bash
pygmentize -l javascript input_file
```

### List available lexers (processors for input languages)

```bash
pygmentize -L lexers
```

### Save output to a file in HTML format

```bash
pygmentize -f html -o output_file.html input_file.py
```

### List available output formats

```bash
pygmentize -L formatters
```

### Output an HTML file, with additional formatter options (full page, with line numbers)

```bash
pygmentize -f html -O "full,linenos=True" -o output_file.html input_file
```
