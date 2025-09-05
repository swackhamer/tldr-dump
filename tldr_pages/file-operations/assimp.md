# assimp

> Client for the Open Asset Import Library. Supports loading of 40+ 3D file formats, and exporting to several popular 3D formats. More information: <https://manned.org/assimp>.

## Examples

### List all supported import formats

```bash
assimp listext
```

### List all supported export formats

```bash
assimp listexport
```

### Convert a file to one of the supported output formats, using the default parameters

```bash
assimp export input_file.stl output_file.obj
```

### Convert a file using custom parameters (the dox_cmd.h file in assimp's source code lists available parameters)

```bash
assimp export input_file.stl output_file.obj parameters
```

### Display a summary of a 3D file's contents

```bash
assimp info path/to/file
```

### Display help

```bash
assimp help
```

### Display help for a specific subcommand

```bash
assimp subcommand --help
```
