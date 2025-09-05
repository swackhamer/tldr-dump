# lynx

> Command-line web browser. More information: <https://lynx.browser.org>.

## Examples

### Visit a website

```bash
lynx example.com
```

### Apply restrictions for anonymous account

```bash
lynx -anonymous example.com
```

### Turn on mouse support, if available

```bash
lynx -use_mouse example.com
```

### Force color mode on, if available

```bash
lynx -color example.com
```

### Open a link, using a specific file to read and write cookies

```bash
lynx -cookie_file=path/to/file example.com
```

### Navigate forwards and backwards through the links on a page

```bash
<ArrowUp>|<ArrowDown>
```

### Go back to the previously displayed page

```bash
<ArrowLeft>|<u>
```

### Exit

```bash
<q><y>
```
