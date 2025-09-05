# linkchecker

> Client to check HTML documents and websites for broken links. More information: <https://linkchecker.github.io/linkchecker/man/linkchecker.html>.

## Examples

### Find broken links on <https://example.com/>

```bash
linkchecker https://example.com/
```

### Also check URLs that point to external domains

```bash
linkchecker --check-extern https://example.com/
```

### Ignore URLs that match a specific `regex`

```bash
linkchecker --ignore-url regex https://example.com/
```

### Output results to a CSV file

```bash
linkchecker --file-output csv/path/to/file https://example.com/
```
