# crane-rebase

> Rebase an image onto a new base image. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

## Examples

### Rebase image

```bash
crane rebase
```

### New base image to insert

```bash
crane rebase --new_base image_name
```

### Old base image to remove

```bash
crane rebase --old_base image_name
```

### Tag to apply to rebased image

```bash
crane rebase [-t|--tag] tag_name
```

### Display help

```bash
crane rebase [-h|--help]
```
