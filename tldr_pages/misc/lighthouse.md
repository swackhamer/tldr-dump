# lighthouse

> Analyzes web applications and web pages, collecting modern performance metrics and insights on developer best practices. More information: <https://github.com/GoogleChrome/lighthouse>.

## Examples

### Generate an HTML report for a specific website and save it to a file in the current directory

```bash
lighthouse https://example.com
```

### Generate a JSON report and print it

```bash
lighthouse --output json https://example.com
```

### Generate a JSON report and save it to a specific file

```bash
lighthouse --output json --output-path path/to/file.json https://example.com
```

### Generate a report using the browser in headless mode without logging to `stdout`

```bash
lighthouse --quiet --chrome-flags="--headless" https://example.com
```

### Generate a report, using the HTTP header key/value pairs in the specified JSON file for all requests

```bash
lighthouse --extra-headers=path/to/file.json https://example.com
```

### Generate a report for specific categories only

```bash
lighthouse --only-categories=performance,accessibility,best-practices,seo,pwa https://example.com
```

### Generate a report with device emulation and all throttling disabled

```bash
lighthouse --screenEmulation.disabled --throttling-method=provided --no-emulatedUserAgent https://example.com
```

### Display help

```bash
lighthouse --help
```
