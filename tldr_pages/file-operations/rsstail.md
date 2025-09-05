# rsstail

> `tail` for RSS feeds. More information: <https://manned.org/rsstail>.

## Examples

### Show the feed of a given URL and wait for new entries appearing at the bottom

```bash
rsstail -u url
```

### Show the feed in reverse chronological order (newer at the bottom)

```bash
rsstail -r -u url
```

### Include publication date and link

```bash
rsstail -pl -u url
```

### Set update interval

```bash
rsstail -u url -i interval_in_seconds
```

### Show feed and exit

```bash
rsstail -1 -u url
```
