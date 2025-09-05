# crane-export

> Export filesystem of a container image as a tarball. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

## Examples

### Write tarball to `stdout`

```bash
crane export image_name -
```

### Write tarball to file

```bash
crane export image_name path/to/tarball
```

### Read image from `stdin`

```bash
crane export - path/to/filename
```
