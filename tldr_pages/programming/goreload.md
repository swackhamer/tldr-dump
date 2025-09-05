# goreload

> Live reload utility for Go programs. More information: <https://github.com/acoshift/goreload>.

## Examples

### Watch a binary file (defaults to `.goreload`)

```bash
goreload [-b|--bin] path/to/binary path/to/file.go
```

### Set a custom log prefix (defaults to `goreload`)

```bash
goreload --logPrefix prefix path/to/file.go
```

### Reload whenever any file changes

```bash
goreload --all
```
