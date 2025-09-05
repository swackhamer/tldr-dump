# blender

> Command-line interface to the Blender 3D computer graphics application. Arguments are executed in the order they are given. More information: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

## Examples

### Render all frames of an animation in the background, without loading the UI (output is saved to `/tmp`)

```bash
blender [-b|--background] path/to/file.blend [-a|--render-anim]
```

### Render an animation using a specific image naming pattern, in a path relative (`//`) to the .blend file

```bash
blender [-b|--background] path/to/file.blend [-o|--render-output] //render/frame_###.png [-a|--render-anim]
```

### Render the 10th frame of an animation as a single image, saved to an existing directory (absolute path)

```bash
blender [-b|--background] path/to/file.blend [-o|--render-output] /path/to/output_directory [-f|--render-frame] 10
```

### Render the second last frame in an animation as a JPEG image, saved to an existing directory (relative path)

```bash
blender [-b|--background] path/to/file.blend [-o|--render-output] //output_directory [-f|--render-frame] JPEG [-f|--render-frame] -2
```

### Render the animation of a specific scene, starting at frame 10 and ending at frame 500

```bash
blender [-b|--background] path/to/file.blend [-S|--scene] scene_name [-s|--frame-start] 10 [-e|--frame-end] 500 [-a|--render-anim]
```

### Render an animation at a specific resolution, by passing a Python expression

```bash
blender [-b|--background] path/to/file.blend --python-expr 'import bpy; bpy.data.scenes[0].render.resolution_percentage = 25' [-a|--render-anim]
```

### Start an interactive Blender session in the terminal with a Python console (do `import bpy` after starting)

```bash
blender [-b|--background] --python-console
```
