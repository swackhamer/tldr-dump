# tag

> Edit tags on Mac OS X files (10.9 Mavericks and above). More information: <https://github.com/jdberry/tag/>.

## Examples

### Add tags to a file

```bash
tag --add tag_name1,tag_name2,... path/to/file
```

### Remove a tag

```bash
tag --remove tag_name path/to/file
```

### Remove all tags from a file

```bash
tag --remove \* path/to/file
```

### Show all files with a given tag

```bash
tag --match tag_name
```
