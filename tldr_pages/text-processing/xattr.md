# xattr

> Utility to work with extended filesystem attributes. More information: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

## Examples

### List key:value extended attributes for a given file

```bash
xattr -l file
```

### Write an attribute for a given file

```bash
xattr -w attribute_key attribute_value file
```

### Delete an attribute from a given file

```bash
xattr -d com.apple.quarantine file
```

### Delete all extended attributes from a given file

```bash
xattr -c file
```

### Recursively delete an attribute in a given directory

```bash
xattr -rd attribute_key directory
```
