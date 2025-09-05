# transcode

> Transcode video and audio codecs, and convert between media formats. More information: <https://manned.org/transcode>.

## Examples

### Create stabilization file to be able to remove camera shakes

```bash
transcode -J stabilize -i input_file
```

### Remove camera shakes after creating stabilization file, transform video using XviD

```bash
transcode -J transform -i input_file -y xvid -o output_file
```

### Resize the video to 640x480 pixels and convert to MPEG4 codec using XviD

```bash
transcode -Z 640x480 -i input_file -y xvid -o output_file
```
