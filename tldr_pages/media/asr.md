# asr

> Restore (copy) a disk image onto a volume. The command name stands for Apple Software Restore. More information: <https://keith.github.io/xcode-man-pages/asr.8.html>.

## Examples

### Restore a disk image to a target volume

```bash
sudo asr restore --source image_file.dmg --target path/to/volume_file
```

### Erase the target volume before restoring

```bash
sudo asr restore --source image_file.dmg --target path/to/volume_file --erase
```

### Skip verification after restoring

```bash
sudo asr restore --source image_file.dmg --target path/to/volume_file --noverify
```

### Clone volumes without using an intermediate disk image

```bash
sudo asr restore --source path/to/volume_file --target path/to/volume_file
```
