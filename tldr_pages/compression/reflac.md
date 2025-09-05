# reflac

> Recompress FLAC files in-place while preserving metadata. More information: <https://github.com/chungy/reflac>.

## Examples

### Recompress a directory of FLAC files

```bash
reflac path/to/directory
```

### Enable maximum compression (very slow)

```bash
reflac [-8|--best] path/to/directory
```

### Display filenames as they are processed

```bash
reflac [-v|--verbose] path/to/directory
```

### Recurse into subdirectories

```bash
reflac [-r|--recursive] path/to/directory
```

### Preserve file modification times

```bash
reflac --preserve path/to/directory
```
