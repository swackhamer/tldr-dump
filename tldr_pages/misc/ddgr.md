# ddgr

> Search DuckDuckGo (HTML version) from the terminal. More information: <https://github.com/jarun/ddgr>.

## Examples

### Start in interactive mode

```bash
ddgr
```

### Search DuckDuckGo for a keyword

```bash
ddgr keyword
```

### Limit the number of search results to `n`

```bash
ddgr [-n|--num] n keyword
```

### Display the complete URL in search results

```bash
ddgr [-x|--expand] keyword
```

### Search DuckDuckGo for a keyword and open the first result in the browser

```bash
ddgr !w keyword
```

### Perform a website-specific search

```bash
ddgr [-w|--site] site keyword
```

### Search for a specific file type

```bash
ddgr keyword filetype:filetype
```

### Display help in interactive mode

```bash
<?>
```
