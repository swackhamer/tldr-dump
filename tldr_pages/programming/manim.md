# manim

> Animation engine for explanatory math videos. More information: <https://docs.manim.community/en/stable/tutorials/quickstart.html>.

## Examples

### Render a scene from a Python script using the default settings

```bash
manim path/to/file.py SceneName
```

### Render with live preview (auto-opens the video file after rendering)

```bash
manim [-pql|--preview --quality low] path/to/file.py SceneName
```

### Render at high quality (1080p 60fps)

```bash
manim [-pqh|--preview --quality high] path/to/file.py SceneName
```

### Specify a custom output file name

```bash
manim [-o|--output_file] output_file_name path/to/file.py SceneName
```

### Render using a specific resolution and frame rate

```bash
manim [-r|--resolution] 1920,1080 [-f|--fps] 60 path/to/file.py SceneName
```

### List available scenes in a file without rendering

```bash
manim --list_scenes path/to/file.py
```

### Display help

```bash
manim --help
```
