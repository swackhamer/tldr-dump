# newsboat

> An RSS/Atom feed reader for text terminals. More information: <https://newsboat.org/releases/2.40/docs/newsboat.html#_first_steps>.

## Examples

### First import feed URLs from an OPML file

```bash
newsboat [-i|--import-from-opml] my-feeds.xml
```

### Alternatively, add feeds manually

```bash
echo http://example.com/path/to/feed >> "${HOME}/.newsboat/urls"
```

### Start Newsboat and refresh all feeds on startup

```bash
newsboat [-r|--refresh-on-start]
```

### Execute one or more commands in non-interactive mode

```bash
newsboat [-x|--execute] reload print-unread ...
```

### See keyboard shortcuts (the most relevant are visible in the status line)

```bash
<?>
```
