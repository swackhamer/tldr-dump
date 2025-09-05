# crane-flatten

> Flatten an image's layers into a single layer. Pushes digest to original image repository if no tags are specified. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

## Examples

### Flatten an image

```bash
crane flatten
```

### Apply new tag to flattened image

```bash
crane flatten [-t|--tag] tag_name
```

### Display help

```bash
crane flatten [-h|--help]
```
