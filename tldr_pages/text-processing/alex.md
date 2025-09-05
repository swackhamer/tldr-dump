# alex

> Catch insensitive, inconsiderate writing. It helps you find gender favouring, polarising, race related, religion inconsiderate, or other unequal phrasing in text. More information: <https://github.com/get-alex/alex>.

## Examples

### Analyze text from `stdin`

```bash
echo His network looks good | alex --stdin
```

### Analyze all files in the current directory

```bash
alex
```

### Analyze a specific file

```bash
alex path/to/file.md
```

### Analyze all Markdown files except `example.md`

```bash
alex *.md !example.md
```
