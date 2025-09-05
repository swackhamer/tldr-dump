# pkgutil

> Query and manipulate Mac OS X Installer packages and receipts. More information: <https://keith.github.io/xcode-man-pages/pkgutil.1.html>.

## Examples

### List package IDs for all installed packages

```bash
pkgutil --pkgs
```

### Verify cryptographic signatures of a package file

```bash
pkgutil --check-signature path/to/filename.pkg
```

### List all the files for an installed package given its ID

```bash
pkgutil --files com.microsoft.Word
```

### Extract the contents of a package file into a directory

```bash
pkgutil --expand-full path/to/filename.pkg path/to/directory
```
