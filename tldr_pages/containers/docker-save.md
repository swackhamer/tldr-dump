# docker-save

> Export Docker images to archive. More information: <https://docs.docker.com/reference/cli/docker/image/save/>.

## Examples

### Save an image by redirecting `stdout` to a tar archive

```bash
docker save image:tag > path/to/file.tar
```

### Save an image to a tar archive

```bash
docker save [-o|--output] path/to/file.tar image:tag
```

### Save all tags of the image

```bash
docker save [-o|--output] path/to/file.tar image_name
```

### Cherry-pick particular tags of an image to save

```bash
docker save [-o|--output] path/to/file.tar image_name:tag1 image_name:tag2 ...
```
