# crane-push

> Push local image contents to a remote registry. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

## Examples

### Push local image to remote registry

```bash
crane push path/to/tarball image_name
```

### Path to file with list of published image references

```bash
crane push path/to/tarball image_name --image-refs path/to/filename
```

### Push a collection of images as a single index (required if path has multiple images)

```bash
crane push path/to/tarball image_name --index
```

### Display help

```bash
crane push [-h|--help]
```
