# buku

> Browser-independent bookmark manager. More information: <https://github.com/jarun/Buku#usage>.

## Examples

### Display all bookmarks matching "keyword" and with "privacy" tag

```bash
buku keyword [-t|--stag] privacy
```

### Add bookmark with tags "search engine" and "privacy"

```bash
buku [-a|--add] https://example.com search engine, privacy
```

### Delete a bookmark

```bash
buku [-d|--delete] bookmark_id
```

### Open editor to edit a bookmark

```bash
buku [-w|--write] bookmark_id
```

### Remove "search engine" tag from a bookmark

```bash
buku [-u|--update] bookmark_id --tag - search engine
```
