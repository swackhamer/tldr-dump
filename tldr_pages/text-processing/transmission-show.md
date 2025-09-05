# transmission-show

> Get information about a torrent file. See also: `transmission`. More information: <https://manned.org/transmission-show>.

## Examples

### Display metadata for a specific torrent

```bash
transmission-show path/to/file.torrent
```

### Generate a magnet link for a specific torrent

```bash
transmission-show [-m|--magnet] path/to/file.torrent
```

### Query a torrent's trackers and print the current number of peers

```bash
transmission-show [-s|--scrape] path/to/file.torrent
```
