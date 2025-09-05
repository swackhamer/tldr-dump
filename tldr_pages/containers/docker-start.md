# docker-start

> Start stopped containers. More information: <https://docs.docker.com/reference/cli/docker/container/start/>.

## Examples

### Display help

```bash
docker start --help
```

### Start a Docker container

```bash
docker start container
```

### Start a container, attaching `stdout` and `stderr` and forwarding signals

```bash
docker start [-a|--attach] container
```

### Start one or more containers

```bash
docker start container1 container2 ...
```
