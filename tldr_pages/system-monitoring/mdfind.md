# mdfind

> List files matching a query. More information: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

## Examples

### Find a file by its name

```bash
mdfind -name file
```

### Find a file by its content

```bash
mdfind "query"
```

### Find a file containing a string, in a given directory

```bash
mdfind -onlyin directory "query"
```
