# gcrane-gc

> List images that are not tagged. Will calculate images that can be garbage-collected. This can be composed with `gcrane delete` to actually garbage collect them. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

## Examples

### List untagged images

```bash
gcrane gc repository
```

### Whether to recurse through repositories

```bash
gcrane gc repository [-r|--recursive]
```

### Display help

```bash
gcrane gc [-h|--help]
```
