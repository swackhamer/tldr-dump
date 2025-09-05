# crane-validate

> Validate that an image is well-formed. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

## Examples

### Validate an image

```bash
crane validate
```

### Skip downloading/digesting layers

```bash
crane validate --fast
```

### Name of remote image to validate

```bash
crane validate --remote image_name
```

### Path to tarball to validate

```bash
crane validate --tarball path/to/tarball
```

### Display help

```bash
crane validate [-h|--help]
```
