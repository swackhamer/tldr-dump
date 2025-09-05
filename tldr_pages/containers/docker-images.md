# docker-images

> Manage Docker images. More information: <https://docs.docker.com/reference/cli/docker/image/ls/>.

## Examples

### List all Docker images

```bash
docker images
```

### List all Docker images including intermediates

```bash
docker images [-a|--all]
```

### List the output in quiet mode (only numeric IDs)

```bash
docker images [-q|--quiet]
```

### List all Docker images not used by any container

```bash
docker images [-f|--filter] dangling=true
```

### List images that contain a substring in their name

```bash
docker images "*name*"
```

### Sort images by size

```bash
docker images --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort [-k|--key] 2 [-h|--human-numeric-sort]
```
