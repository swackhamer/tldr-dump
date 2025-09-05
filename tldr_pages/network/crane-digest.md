# crane-digest

> Get the digest of an image. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

## Examples

### Get the digest of an image

```bash
crane digest image_name
```

### Print the full image reference by digest

```bash
crane digest image_name --full-ref
```

### Specify path to tarball containing the image

```bash
crane digest image_name --tarball path/to/tarball
```

### Display help

```bash
crane digest [-h|--help]
```
