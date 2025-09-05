# exiftool

> Read and write meta information in files. More information: <https://exiftool.org>.

## Examples

### Print the EXIF metadata for a given file

```bash
exiftool path/to/file
```

### Remove all EXIF metadata from the given files

```bash
exiftool -All= path/to/file1 path/to/file2 ...
```

### Remove GPS EXIF metadata from given image files

```bash
exiftool "-gps*=" path/to/image1 path/to/image2 ...
```

### Remove all EXIF metadata from the given image files, then re-add metadata for color and orientation

```bash
exiftool -All= -tagsfromfile @ -colorspacetags -orientation path/to/image1 path/to/image2 ...
```

### Move the date at which all photos in a directory were taken 1 hour forward

```bash
exiftool "-AllDates+=0:0:0 1:0:0" path/to/directory
```

### Move the date at which all JPEG photos in the current directory were taken 1 day and 2 hours backward

```bash
exiftool "-AllDates-=0:0:1 2:0:0" [-ext|-extension] jpg
```

### Only change the `DateTimeOriginal` field subtracting 1.5 hours, without keeping backups

```bash
exiftool -DateTimeOriginal-=1.5 -overwrite_original
```

### Recursively rename all JPEG photos in a directory based on the `DateTimeOriginal` field

```bash
exiftool '-filename<DateTimeOriginal' [-d|-dateFormat] %Y-%m-%d_%H-%M-%S%%lc.%%e path/to/directory [-r|-recurse] [-ext|-extension] jpg
```
