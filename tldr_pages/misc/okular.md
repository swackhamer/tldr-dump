# okular

> View documents. More information: <https://docs.kde.org/stable5/en/okular/okular/command-line-options.html>.

## Examples

### Launch document viewer

```bash
okular
```

### Open specific documents

```bash
okular path/to/file1 path/to/file2 ...
```

### Open a document at a specific page

```bash
okular [-p|--page] page_number path/to/file
```

### Open a specific document in presentation mode

```bash
okular --presentation path/to/file
```

### Open a specific document and start a print dialog

```bash
okular --print path/to/file
```

### Open a document and search for a specific string

```bash
okular --find search_string path/to/file
```
