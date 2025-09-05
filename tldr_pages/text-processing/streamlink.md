# streamlink

> Extracts streams from various services and pipes them into a video player of choice. More information: <https://streamlink.github.io>.

## Examples

### Attempt to extract streams from the URL specified, and if it's successful, print out a list of available streams to choose from

```bash
streamlink example.com/stream
```

### Open a stream with the specified quality

```bash
streamlink example.com/stream 720p60
```

### Select the highest or lowest available quality

```bash
streamlink example.com/stream best|worst
```

### Use a specific player to feed stream data to (VLC is used by default if found)

```bash
streamlink --player=mpv example.com/stream best
```

### Skip a specific amount of time from the beginning of the stream. For live streams, this is a negative offset from the end of the stream (rewind)

```bash
streamlink --hls-start-offset [HH:]MM:SS example.com/stream best
```

### Skip to the beginning of a live stream, or as far back as possible

```bash
streamlink --hls-live-restart example.com/stream best
```

### Write stream data to a file instead of playing it

```bash
streamlink --output path/to/file.ts example.com/stream best
```

### Open the stream in the player, while at the same time writing it to a file

```bash
streamlink --record path/to/file.ts example.com/stream best
```
