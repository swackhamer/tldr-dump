# gst-inspect-1.0

> Print information on GStreamer plugins. More information: <https://gstreamer.freedesktop.org/documentation/tools/gst-inspect.html>.

## Examples

### Print information on a plugin

```bash
gst-inspect-1.0 plugin
```

### List hardware transcoding capabilities of your device

```bash
gst-inspect-1.0 vaapi|nvcodec|...
```

### List available container plugins

```bash
gst-inspect-1.0 matroska|avi|ogg|isomp4|...
```

### List available audio codecs

```bash
gst-inspect-1.0 opus|vorbis|flac|...
```

### List GStreamer core elements

```bash
gst-inspect-1.0 coreelements
```

### List plugins that utilize graphics APIs

```bash
gst-inspect-1.0 vulkan|opengl|...
```

### List available image codecs

```bash
gst-inspect-1.0 png|jpeg|...
```

### List all available plugins

```bash
gst-inspect-1.0
```
