# unar

> Extract contents from archive files. More information: <https://manned.org/unar>.

## Examples

### Extract an archive to the current directory

```bash
unar path/to/archive
```

### Extract an archive to the specified directory

```bash
unar [-o|-output-directory] path/to/directory path/to/archive
```

### Force overwrite if files to be unpacked already exist

```bash
unar [-f|-force-overwrite] path/to/archive
```

### Force rename if files to be unpacked already exist

```bash
unar [-r|-force-rename] path/to/archive
```

### Force skip if files to be unpacked already exist

```bash
unar [-s|-force-skip] path/to/archive
```
