# peerflix

> Stream video- or audio-based torrents to a media player. More information: <https://github.com/mafintosh/peerflix>.

## Examples

### Stream the largest media file in a torrent

```bash
peerflix "torrent_url|magnet_link"
```

### List all streamable files contained in a torrent (given as a magnet link)

```bash
peerflix "magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567" [-l|--list]
```

### Stream the largest file in a torrent, given as a torrent URL, to VLC

```bash
peerflix "http://example.net/music.torrent" [-v|--vlc]
```

### Stream the largest file in a torrent to MPlayer, with subtitles

```bash
peerflix "torrent_url|magnet_link" [-m|--mplayer] [-t|--subtitles] subtitle-file.srt
```

### Stream all files from a torrent to Airplay

```bash
peerflix "torrent_url|magnet_link" [-a|--all] [-s|--airplay]
```
