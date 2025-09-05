# lychee

> Find broken URLs. More information: <https://github.com/lycheeverse/lychee/blob/master/README.md#commandline-usage>.

## Examples

### Scan a website for broken links

```bash
lychee https://example.com
```

### Display a breakdown of error types

```bash
lychee --format detailed https://example.com
```

### Limit the amount of connections to prevent DDOS protection

```bash
lychee --max-concurrency 5 links.txt
```

### Check files in a directory structure for any broken URLs

```bash
grep [-r|--recursive] "pattern" | lychee -
```

### Display help

```bash
lychee --help
```
