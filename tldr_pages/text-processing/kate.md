# kate

> KDE's advanced text editor. More information: <https://docs.kde.org/stable/en/kate/kate/fundamentals.html#starting-from-the-command-line>.

## Examples

### Open specific files

```bash
kate path/to/file1 path/to/file2 ...
```

### Open specific remote files

```bash
kate https://example.com/path/to/file1 https://example.com/path/to/file2 ...
```

### Create a new editor instance even if one is already open

```bash
kate [-n|--new]
```

### Open a file with the cursor at the specific line

```bash
kate [-l|--line] line_number path/to/file
```

### Open a file with the cursor at the specific line and column

```bash
kate [-l|--line] line_number [-c|--column] column_number path/to/file
```

### Create a file from `stdin`

```bash
cat path/to/file | kate [-i|--stdin]
```

### Display help

```bash
kate [-h|--help]
```
