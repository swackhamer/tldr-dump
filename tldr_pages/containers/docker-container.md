# docker-container

> Manage Docker containers. More information: <https://docs.docker.com/reference/cli/docker/container/>.

## Examples

### List currently running Docker containers

```bash
docker container ls
```

### Start one or more stopped containers

```bash
docker container start container1_name container2_name
```

### Kill one or more running containers

```bash
docker container kill container_name
```

### Stop one or more running containers

```bash
docker container stop container_name
```

### Pause all processes within one or more containers

```bash
docker container pause container_name
```

### Display detailed information on one or more containers

```bash
docker container inspect container_name
```

### Export a container's filesystem as a tar archive

```bash
docker container export container_name
```

### Create a new image from a container's changes

```bash
docker container commit container_name
```
