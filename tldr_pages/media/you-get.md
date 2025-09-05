# you-get

> Download media contents (videos, audios, images) from the Web. See also: `yt-dlp`, `youtube-viewer`, `instaloader`. More information: <https://you-get.org>.

## Examples

### Print media information about a specific media on the web

```bash
you-get --info https://example.com/video?id=value
```

### Download a media from a specific URL

```bash
you-get https://example.com/video?id=value
```

### Search on Google Videos and download

```bash
you-get keywords
```

### Download a media to a specific location

```bash
you-get --output-dir path/to/directory --output-filename filename https://example.com/watch?v=value
```

### Download a media using a proxy

```bash
you-get --http-proxy proxy_server https://example.com/watch?v=value
```
