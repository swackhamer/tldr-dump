# spotdl

> Download Spotify playlists and songs along with metadata. More information: <https://github.com/spotDL/spotify-downloader>.

## Examples

### Download songs from the provided URLs and embed metadata

```bash
spotdl open.spotify.com/playlist/playlistId1 open.spotify.com/track/trackId2 ...
```

### Start a web interface to download individual songs

```bash
spotdl web
```

### Save only the metadata without downloading anything

```bash
spotdl save open.spotify.com/playlist/playlistId1 open.spotify.com/track/trackId2 ... --save-file path/to/save_file.spotdl
```
