# crane-tag

> Efficiently tag a remote image without downloading it, which differs from the `copy` command. It skips the layer existence checks because we know the manifest already exists making it slightly faster. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

## Examples

### Tag remote image

```bash
crane tag image_name tag_name
```

### Display help

```bash
crane tag [-h|--help]
```
