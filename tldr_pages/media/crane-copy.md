# crane-copy

> Efficiently copy a remote image from source to target while retaining the digest value. More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

## Examples

### Copy an image from source to target

```bash
crane copy source target
```

### Copy all tags

```bash
crane copy source target [-a|--all-tags]
```

### Set the maximum number of concurrent copies, defaults to GOMAXPROCS

```bash
crane copy source target [-j|--jobs] int
```

### Avoid overwriting existing tags in target

```bash
crane copy source target [-n|--no-clobber]
```

### Display help

```bash
crane copy [-h|--help]
```
