# docker-load

> Load Docker images from files or `stdin`. More information: <https://docs.docker.com/reference/cli/docker/image/load/>.

## Examples

### Load a Docker image from `stdin`

```bash
docker load < path/to/image_file.tar
```

### Load a Docker image from a specific file

```bash
docker load [-i|--input] path/to/image_file.tar
```

### Load a Docker image from a specific file in quiet mode

```bash
docker load [-q|--quiet] [-i|--input] path/to/image_file.tar
```
