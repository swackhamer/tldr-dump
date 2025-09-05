# ntfs-read.py

> A read-only NTFS explorer for accessing and extracting files from NTFS volumes. Part of the Impacket suite. More information: <https://github.com/fortra/impacket>.

## Examples

### Open an NTFS volume for exploration (e.g., `C:\.\\` or `/dev/disk1s1`)

```bash
ntfs-read.py volume
```

### Extract a specific file from an NTFS volume (e.g., `\windows\system32\config\sam`)

```bash
ntfs-read.py -extract \windows\system32\config\sam volume
```

### Enable debug output

```bash
ntfs-read.py -debug volume
```

### Display help

```bash
ntfs-read.py --help
```
