# exiv2

> Image metadata manipulation tool. More information: <https://www.exiv2.org/manpage.html>.

## Examples

### Print a summary of the image Exif metadata

```bash
exiv2 path/to/file
```

### Print all metadata (Exif, IPTC, XMP) with interpreted values

```bash
exiv2 [-P|-Print] kt path/to/file
```

### Print all metadata with raw values

```bash
exiv2 [-P|-Print] kv path/to/file
```

### Delete all metadata from an image

```bash
exiv2 [-d|--delete] a path/to/file
```

### Delete all metadata, preserving the file timestamp

```bash
exiv2 [-d|--delete] a [-k|--keep] path/to/file
```

### Rename the file, prepending the date and time from metadata (not from the file timestamp)

```bash
exiv2 [-r|--rename] '%Y%m%d_%H%M%S_:basename:' path/to/file
```
