# deluge

> A BitTorrent client. More information: <https://manned.org/deluge>.

## Examples

### Download a torrent

```bash
deluge url|magnet|path/to/file
```

### Download a torrent using a specific configuration file

```bash
deluge [-c|--config] path/to/configuration_file url|magnet|path/to/file
```

### Download a torrent and launch the specified user interface

```bash
deluge -u gtk|web|console url|magnet|path/to/file
```

### Download a torrent and output the log to a file

```bash
deluge [-l|--logfile] path/to/log_file url|magnet|path/to/file
```
