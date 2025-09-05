# docker-commit

> Create a new image from a container's changes. More information: <https://docs.docker.com/reference/cli/docker/container/commit/>.

## Examples

### Create an image from a specific container

```bash
docker commit container image:tag
```

### Apply a `CMD` Dockerfile instruction to the created image

```bash
docker commit [-c|--change] "CMD command" container image:tag
```

### Apply an `ENV` Dockerfile instruction to the created image

```bash
docker commit [-c|--change] "ENV name=value" container image:tag
```

### Create an image with a specific author in the metadata

```bash
docker commit [-a|--author] "author" container image:tag
```

### Create an image with a specific comment in the metadata

```bash
docker commit [-m|--message] "comment" container image:tag
```

### Create an image without pausing the container during commit

```bash
docker commit [-p|--pause] false container image:tag
```

### Display help

```bash
docker commit --help
```
