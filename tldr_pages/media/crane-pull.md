# crane-pull

> Pull remote images by reference and store their contents locally. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

## Examples

### Pull remote image

```bash
crane pull image_name path/to/tarball
```

### Preserve image reference used to pull as an annotation when used with --format=oci

```bash
crane pull image_name path/to/tarball --annotate-ref
```

### Path to cache image layers

```bash
crane pull image_name path/to/tarball [-c|--cache_path] path/to/cache
```

### Format in which to save images (default 'tarball')

```bash
crane pull image_name path/to/tarball -format format_name
```

### Display help

```bash
crane pull [-h|--help]
```
