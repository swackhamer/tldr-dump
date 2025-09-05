# hdiutil

> Utility to create and manage disk images. More information: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

## Examples

### Mount an image

```bash
hdiutil attach path/to/image_file
```

### Unmount an image

```bash
hdiutil detach /Volumes/volume_file
```

### List mounted images

```bash
hdiutil info
```

### Create an ISO image from the contents of a directory

```bash
hdiutil makehybrid -o path/to/output_file path/to/directory
```
