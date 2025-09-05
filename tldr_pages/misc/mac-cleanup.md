# mac-cleanup

> A modern macOS cleanup tool to remove caches and junk. More information: <https://github.com/mac-cleanup/mac-cleanup-py>.

## Examples

### Start the cleanup process

```bash
mac-cleanup
```

### Open the module configuration screen

```bash
mac-cleanup [-c|--configure]
```

### Perform a dry-run, showing what will be removed without actually deleting it

```bash
mac-cleanup [-n|--dry-run]
```

### Specify the directory with custom cleanup path

```bash
mac-cleanup [-p|--custom-path] path/to/directory
```

### Automatically acknowledge all warnings and continue with force

```bash
mac-cleanup [-f|--force]
```
