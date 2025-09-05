# mpv

> A audio/video player based on MPlayer. See also: `mplayer`, `vlc`. More information: <https://mpv.io/manual/stable/>.

## Examples

### Play a video or audio from a URL or file

```bash
mpv url|path/to/file
```

### Jump backward/forward 5 seconds

```bash
<ArrowLeft>|<ArrowRight>
```

### Jump backward/forward 1 minute

```bash
<ArrowDown>|<ArrowUp>
```

### Decrease or increase playback speed by 10%

```bash
<[>|<]>
```

### Add subtitles from a file

```bash
mpv --sub-file=path/to/file
```

### Take a screenshot of the current frame (saved to `./mpv-shotNNNN.jpg` by default)

```bash
<s>
```

### Play a file at a specified speed (1 by default)

```bash
mpv --speed 0.01..100 path/to/file
```

### Play a file using a profile defined in the `mpv.conf` file

```bash
mpv --profile profile_name path/to/file
```
