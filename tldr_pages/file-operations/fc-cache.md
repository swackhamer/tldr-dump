# fc-cache

> Scan font directories to build font cache files. More information: <https://manned.org/fc-cache>.

## Examples

### Generate font cache files

```bash
fc-cache
```

### Generate font cache files verbosely

```bash
fc-cache [-v|--verbose]
```

### Force a rebuild of all font cache files, without checking if cache is up-to-date

```bash
fc-cache [-f|--force]
```

### Erase font cache files, then generate new font cache files

```bash
fc-cache [-r|--really-force]
```

### Scan a specific directory

```bash
fc-cache path/to/directory
```

### Scan system-wide directories, skipping the user's home directory

```bash
fc-cache [-s|--system-only]
```

### Display version

```bash
fc-cache [-V|--version]
```
