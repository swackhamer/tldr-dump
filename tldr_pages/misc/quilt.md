# quilt

> Manage a series of patches. More information: <https://manned.org/quilt>.

## Examples

### Import an existing patch from a file

```bash
quilt import path/to/filename.patch
```

### Create a new patch

```bash
quilt new filename.patch
```

### Add a file to the current patch

```bash
quilt add path/to/file
```

### After editing the file, refresh the current patch with the changes

```bash
quilt refresh
```

### Apply all the patches in the series file

```bash
quilt push -a
```

### Remove all applied patches

```bash
quilt pop -a
```
