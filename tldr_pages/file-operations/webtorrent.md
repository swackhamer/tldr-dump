# webtorrent

> The interface for WebTorrent. Supports magnets, URLs, info hashes and `.torrent` files. More information: <https://github.com/webtorrent/webtorrent-cli>.

## Examples

### Download a torrent

```bash
webtorrent download "torrent_id"
```

### Stream a torrent to VLC media player

```bash
webtorrent download "torrent_id" --vlc
```

### Stream a torrent to a Digital Living Network Alliance (DLNA) device

```bash
webtorrent download "torrent_id" --dlna
```

### Display a list of files for a specific torrent

```bash
webtorrent download "torrent_id" --select
```

### Specify a file index from the torrent to download

```bash
webtorrent download "torrent_id" --select index
```

### Seed a specific file or directory

```bash
webtorrent seed path/to/file_or_directory
```

### Create a new torrent file for the specified file path

```bash
webtorrent create path/to/file
```

### Display information for a magnet URI or `.torrent` file

```bash
webtorrent info path/to/file_or_magnet
```
