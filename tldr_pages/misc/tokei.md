# tokei

> Display statistics about code. More information: <https://github.com/XAMPPRocky/tokei>.

## Examples

### Display a report for the code in a directory and all subdirectories

```bash
tokei path/to/directory
```

### Display a report for a directory excluding `.min.js` files

```bash
tokei path/to/directory [-e|--exclude] *.min.js
```

### Display statistics for individual files in a directory

```bash
tokei path/to/directory [-f|--files]
```

### Display a report for all files of type Rust and Markdown

```bash
tokei path/to/directory [-t|--type] Rust,Markdown
```
