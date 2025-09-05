# docker

> Manage Docker containers and images. Some subcommands such as `run` have their own usage documentation. More information: <https://docs.docker.com/reference/cli/docker/>.

## Examples

### List all Docker containers (running and stopped)

```bash
docker ps [-a|--all]
```

### Start a container from an image, with a custom name

```bash
docker run --name container_name image
```

### Start or stop an existing container

```bash
docker start|stop container_name
```

### Pull an image from a Docker registry

```bash
docker pull image
```

### Display the list of already downloaded images

```bash
docker images
```

### Open an interactive tty with Bourne shell (`sh`) inside a running container

```bash
docker exec [-it|--interactive --tty] container_name sh
```

### Remove stopped containers

```bash
docker rm container1 container2 ...
```

### Fetch and follow the logs of a container

```bash
docker logs [-f|--follow] container_name
```
