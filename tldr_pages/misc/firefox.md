# firefox

> A free and open source web browser. More information: <https://wiki.mozilla.org/Firefox/CommandLineOptions>.

## Examples

### Launch Firefox and open a web page

```bash
firefox https://www.duckduckgo.com
```

### Open a new window

```bash
firefox --new-window https://www.duckduckgo.com
```

### Open a private (incognito) window

```bash
firefox --private-window
```

### Search for "wikipedia" using the default search engine

```bash
firefox --search "wikipedia"
```

### Launch Firefox in safe mode, with all extensions disabled

```bash
firefox --safe-mode
```

### Take a screenshot of a web page in headless mode

```bash
firefox --headless --screenshot path/to/output_file.png https://example.com/
```

### Use a specific profile to allow multiple separate instances of Firefox to run at once

```bash
firefox --profile path/to/directory https://example.com/
```

### Set Firefox as the default browser

```bash
firefox --setDefaultBrowser
```
