# wcurl

> A simple wrapper around `curl` to easily download files. See also: `curl`. More information: <https://curl.se/wcurl/manual.html>.

## Examples

### Download the contents of a URL to a file indicated by the URL ("foo" in this case)

```bash
wcurl https://example.com/foo
```

### Download the contents of a URL to a file with a specified name

```bash
wcurl [-o|--output] bar https://example.com/foo
```

### Download the contents of a URL, enabling progress bar and defaulting to HTTP/2

```bash
wcurl --curl-options "--progress-bar --http2" https://example.com/foo
```

### Resume from an interrupted download

```bash
wcurl --curl-options "--continue-at -" https://example.com/foo
```
