# pr

> Paginate or columnate files for printing. More information: <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

## Examples

### Print multiple files with a default header and footer

```bash
pr path/to/file1 path/to/file2 ...
```

### Print with a custom centered header

```bash
pr [-h|--header] "header" path/to/file1 path/to/file2 ...
```

### Print with numbered lines and a custom date format

```bash
pr [-n|--number-lines] [-D|--date-format] "format" path/to/file1 path/to/file2 ...
```

### Print all files together, one in each column, without a header or footer

```bash
pr [-m|--merge] [-T|--omit-pagination] path/to/file1 path/to/file2 ...
```

### Print, beginning at page 2 up to page 5, with a given page length (including header and footer)

```bash
pr +2:5 [-l|--length] page_length path/to/file1 path/to/file2 ...
```

### Print with an offset for each line and a truncating custom page width

```bash
pr [-o|--indent] offset [-W|--page_width] width path/to/file1 path/to/file2 ...
```
