# yt-dlp

> A youtube-dl fork with additional features and fixes. Download videos from YouTube and other websites. See also: `ytfzf`. More information: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

## Examples

### Download a video or playlist (with the default options from command below)

```bash
yt-dlp "https://www.youtube.com/watch?v=oHg5SJYRHA0"
```

### List the available downloadable formats for a video

```bash
yt-dlp [-F|--list-formats] "https://www.youtube.com/watch?v=oHg5SJYRHA0"
```

### Download a video or playlist using the best MP4 video available (default is "bv\*+ba/b")

```bash
yt-dlp [-f|--format] "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" "https://www.youtube.com/watch?v=oHg5SJYRHA0"
```

### Extract audio from a video (requires ffmpeg or ffprobe)

```bash
yt-dlp [-x|--extract-audio] "https://www.youtube.com/watch?v=oHg5SJYRHA0"
```

### Specify audio format and audio quality of extracted audio (between 0 (best) and 10 (worst), default = 5)

```bash
yt-dlp [-x|--extract-audio] --audio-format mp3 --audio-quality 0 "https://www.youtube.com/watch?v=oHg5SJYRHA0"
```

### Download only the second, fourth, fifth, sixth, and last items in a playlist (the first item is 1, not 0)

```bash
yt-dlp [-I|--playlist-items] 2,4:6,-1 "https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA"
```

### Download all playlists of a YouTube channel/user keeping each playlist in a separate directory

```bash
yt-dlp [-o|--output] "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/user/TheLinuxFoundation/playlists"
```

### Download a Udemy course keeping each chapter in a separate directory

```bash
yt-dlp [-u|--username] user [-p|--password] password [-P|--paths] "path/to/directory" [-o|--output] "%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s" "https://www.udemy.com/java-tutorial"
```
