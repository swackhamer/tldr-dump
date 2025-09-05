# plutil

> View, convert, validate, or edit property list ("plist") files. More information: <https://keith.github.io/xcode-man-pages/plutil.1.html>.

## Examples

### Display the contents of one or more plist files in human-readable format

```bash
plutil -p file1.plist file2.plist ...
```

### Convert one or more plist files to XML format, overwriting the original files in-place

```bash
plutil -convert xml1 file1.plist file2.plist ...
```

### Convert one or more plist files to binary format, overwriting the original files in-place

```bash
plutil -convert binary1 file1.plist file2.plist ...
```

### Convert a plist file to a different format, writing to a new file

```bash
plutil -convert xml1|binary1|json|swift|objc path/to/file.plist -o path/to/new_file.plist
```

### Convert a plist file to a different format, writing to `stdout`

```bash
plutil -convert xml1|binary1|json|swift|objc path/to/file.plist -o -
```
