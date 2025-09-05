# gcrane-ls

> List the tags in a repository. More complex form than `crane ls`, which allows for listing tags, manifest and sub-repositories. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

## Examples

### List the tags

```bash
gcrane ls repository
```

### Format response from the registry as JSON

```bash
gcrane ls repository --json
```

### Whether to recurse through repositories

```bash
gcrane ls repository [-r|--recursive]
```

### Display help

```bash
gcrane ls [-h|--help]
```
