# deluge-console

> An interactive interface for the Deluge BitTorrent client. More information: <https://deluge-torrent.org/userguide/thinclient/>.

## Examples

### Start the interactive console interface

```bash
deluge-console
```

### Connect to a Deluge daemon instance

```bash
connect hostname:port
```

### Add a torrent to the daemon

```bash
add url|magnet|path/to/file
```

### Display information about all torrents

```bash
info
```

### Display information about a specific torrent

```bash
info torrent_id
```

### Pause a torrent

```bash
pause torrent_id
```

### Resume a torrent

```bash
resume torrent_id
```

### Remove a torrent from the daemon

```bash
rm torrent_id
```
