# calibredb

> Manipulate an e-book database. Part of the Calibre e-book library. More information: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

## Examples

### List e-books in the library with additional information

```bash
calibredb list
```

### Search for e-books displaying additional information

```bash
calibredb list --search search_term
```

### Search for just ids of e-books

```bash
calibredb search search_term
```

### Add one or more e-books to the library

```bash
calibredb add path/to/file1 path/to/file2 ...
```

### Recursively add all e-books under a directory to the library

```bash
calibredb add [-r|--recurse] path/to/directory
```

### Remove one or more e-books from the library. You need the e-book IDs (see above)

```bash
calibredb remove id1 id2 ...
```
