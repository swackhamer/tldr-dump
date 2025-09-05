# x_x

> View Excel and CSV files. More information: <https://github.com/kristianperkins/x_x>.

## Examples

### View an XLSX or CSV file

```bash
x_x file.xlsx|file.csv
```

### View an XLSX or CSV file, using the first row as table headers

```bash
x_x [-h|--heading] 0 file.xlsx|file.csv
```

### View a CSV file with unconventional delimiters

```bash
x_x [-d|--delimiter] ';' [-q|--quotechar] '|' file.csv
```
