# enscript

> Convert text files to PostScript, HTML, RTF, ANSI, and overstrikes. More information: <https://manned.org/enscript>.

## Examples

### Generate a PostScript file from a text file

```bash
enscript path/to/input_file [-o|--output] path/to/output_file
```

### Generate a file in a different language than PostScript

```bash
enscript path/to/input_file [-w|--language] html|rtf|... [-o|--output] path/to/output_file
```

### Generate a PostScript file with a landscape layout, splitting the page into columns (maximum 9)

```bash
enscript path/to/input_file --columns num [-r|--landscape] [-o|--output] path/to/output_file
```

### Display available syntax highlighting languages and file formats

```bash
enscript --help-highlight
```

### Generate a PostScript file with syntax highlighting and color for a specified language

```bash
enscript path/to/input_file --color 1 [-E|--highlight] language [-o|--output] path/to/output_file
```
