# shiori

> Simple bookmark manager built with Go. More information: <https://github.com/go-shiori/shiori/blob/master/docs/Usage.md>.

## Examples

### Import bookmarks from HTML Netscape bookmark format file

```bash
shiori import path/to/bookmarks.html
```

### Save the specified URL as bookmark

```bash
shiori add url
```

### List the saved bookmarks

```bash
shiori print
```

### Open the saved bookmark in a browser

```bash
shiori open bookmark_id
```

### Start the web interface for managing bookmarks at port 8181

```bash
shiori serve --port 8181
```
