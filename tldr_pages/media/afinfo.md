# afinfo

> Audio file metadata parser for OS X. Built-in command of OS X. More information: <https://keith.github.io/xcode-man-pages/afinfo.1.html>.

## Examples

### Display info of a given audio file

```bash
afinfo path/to/file
```

### Print a one line description of the audio file

```bash
afinfo --brief path/to/file
```

### Print metadata info and contents of the audio file's InfoDictionary

```bash
afinfo --info path/to/file
```

### Print output in XML format

```bash
afinfo --xml path/to/file
```

### Print warnings for the audio file if any

```bash
afinfo --warnings path/to/file
```

### Display help

```bash
afinfo --help
```
