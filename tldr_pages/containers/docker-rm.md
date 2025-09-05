# docker-rm

> Remove containers. More information: <https://docs.docker.com/reference/cli/docker/container/rm/>.

## Examples

### Remove containers

```bash
docker rm container1 container2 ...
```

### Force remove a container

```bash
docker rm [-f|--force] container1 container2 ...
```

### Remove a container and its volumes

```bash
docker rm [-v|--volumes] container
```

### Display help

```bash
docker rm [-h|--help]
```
