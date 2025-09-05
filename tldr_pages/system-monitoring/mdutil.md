# mdutil

> Manage the metadata stores used by Spotlight for indexing. More information: <https://keith.github.io/xcode-man-pages/mdutil.1.html>.

## Examples

### Show the indexing status of the startup volume

```bash
mdutil -s /
```

### Turn on/off the Spotlight indexing for a given volume

```bash
mdutil -i on|off path/to/volume
```

### Turn on/off indexing for all volumes

```bash
mdutil -a -i on|off
```

### Erase the metadata stores and restart the indexing process

```bash
mdutil -E path/to/volume
```
