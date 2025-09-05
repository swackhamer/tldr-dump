# docker-image

> Manage Docker images. See also: `docker build`, `docker import`, `docker pull`. More information: <https://docs.docker.com/reference/cli/docker/image/>.

## Examples

### List local Docker images

```bash
docker image ls
```

### Delete unused local Docker images

```bash
docker image prune
```

### Delete all unused images (not just those without a tag)

```bash
docker image prune [-a|--all]
```

### Show the history of a local Docker image

```bash
docker image history image
```

### View documentation for `docker image rm`

```bash
tldr docker rmi
```
