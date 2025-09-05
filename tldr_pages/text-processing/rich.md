# rich

> A toolbox for fancy output in the terminal. More information: <https://github.com/Textualize/rich-cli>.

## Examples

### Display a file with syntax highlighting

```bash
rich path/to/file.py
```

### Add line numbers, and indentation guides

```bash
rich path/to/file.py --line-numbers --guides
```

### Apply a theme

```bash
rich path/to/file.py --theme monokai
```

### Display a file in an interactive pager

```bash
rich path/to/file.py --pager
```

### Display contents from a URL

```bash
rich https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md --markdown --pager
```

### Export a file as HTML

```bash
rich path/to/file.md --export-html path/to/file.html
```

### Display text with formatting tags, custom alignment, and line width

```bash
rich --print "Hello [green on black]Stylized[/green on black] [bold]World[/bold]" --left|center|right --width 10
```
