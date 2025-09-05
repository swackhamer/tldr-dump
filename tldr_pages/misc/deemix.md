# deemix

> A barebone deezer downloader library built from the ashes of Deezloader Remix. It can be used as a standalone CLI app or implemented in a UI using the API. More information: <https://gitlab.com/RemixDev/deemix-py>.

## Examples

### Download a track or playlist

```bash
deemix https://www.deezer.com/us/track/00000000
```

### Download track/playlist at a specific bitrate

```bash
deemix --bitrate FLAC|MP3 url
```

### Download to a specific path

```bash
deemix --bitrate bitrate --path path url
```

### Create a portable deemix configuration file in the current directory

```bash
deemix --portable --bitrate bitrate --path path url
```
