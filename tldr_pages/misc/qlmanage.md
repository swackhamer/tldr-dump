# qlmanage

> QuickLook server tool. More information: <https://keith.github.io/xcode-man-pages/qlmanage.1.html>.

## Examples

### Display QuickLook for one or multiple files

```bash
qlmanage -p path/to/file1 path/to/file2 ...
```

### Compute 300px wide PNG thumbnails of all JPEGs in the current directory and put them in a directory

```bash
qlmanage *.jpg -t -s 300 path/to/directory
```

### Reset QuickLook

```bash
qlmanage -r
```
