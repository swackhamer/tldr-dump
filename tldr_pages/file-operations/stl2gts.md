# stl2gts

> Convert STL files into the GTS (GNU triangulated surface library) file format. More information: <https://manned.org/stl2gts>.

## Examples

### Convert an STL file to a GTS file

```bash
stl2gts < path/to/file.stl > path/to/file.gts
```

### Convert an STL file to a GTS file and revert face normals

```bash
stl2gts --revert < path/to/file.stl > path/to/file.gts
```

### Convert an STL file to a GTS file and do not merge vertices

```bash
stl2gts --nomerge < path/to/file.stl > path/to/file.gts
```

### Convert an STL file to a GTS file and display surface statistics

```bash
stl2gts --verbose < path/to/file.stl > path/to/file.gts
```

### Display help

```bash
stl2gts --help
```
