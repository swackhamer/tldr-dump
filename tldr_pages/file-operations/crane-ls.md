# crane-ls

> List the tags in a repository. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_ls.md>.

## Examples

### List the tags

```bash
crane ls repository
```

### Print the full image reference

```bash
crane ls repository --full-ref
```

### Omit digest tags

```bash
crane ls [-o|--omit-digest-tags]
```

### Display help

```bash
crane ls [-h|--help]
```
