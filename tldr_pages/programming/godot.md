# godot

> An open source 2D and 3D game engine. More information: <https://docs.godotengine.org/en/latest/tutorials/editor/command_line_tutorial.html>.

## Examples

### Run a project if the current directory contains a `project.godot` file, otherwise open the project manager

```bash
godot
```

### Edit a project (the current directory must contain a `project.godot` file)

```bash
godot [-e|--editor]
```

### Open the project manager even if the current directory contains a `project.godot` file

```bash
godot [-p|--project-manager]
```

### Export a project for release using a given export preset (the preset must be defined in the project)

```bash
godot --export-release preset output_path
```

### Execute a standalone GDScript file (the script must inherit from `SceneTree` or `MainLoop`)

```bash
godot [-s|--script] script.gd
```
