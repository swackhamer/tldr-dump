# cmark

> Convert CommonMark Markdown formatted text to other formats. More information: <https://github.com/commonmark/cmark>.

## Examples

### Render a CommonMark Markdown file to HTML

```bash
cmark --to html filename.md
```

### Convert data from `stdin` to LaTeX

```bash
cmark --to latex
```

### Convert straight quotes to smart quotes

```bash
cmark --smart --to html filename.md
```

### Validate UTF-8 characters

```bash
cmark --validate-utf8 filename.md
```
