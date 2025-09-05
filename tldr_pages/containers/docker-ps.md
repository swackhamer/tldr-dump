# docker-ps

> List Docker containers. More information: <https://docs.docker.com/reference/cli/docker/container/ls/>.

## Examples

### List currently running Docker containers

```bash
docker ps
```

### List all Docker containers (running and stopped)

```bash
docker ps [-a|--all]
```

### Show the latest created container (includes all states)

```bash
docker ps [-l|--latest]
```

### Filter containers that contain a substring in their name

```bash
docker ps [-f|--filter] "name=name"
```

### Filter containers that share a given image as an ancestor

```bash
docker ps [-f|--filter] "ancestor=image:tag"
```

### Filter containers by exit status code

```bash
docker ps [-a|--all] [-f|--filter] "exited=code"
```

### Filter containers by status (created, running, removing, paused, exited and dead)

```bash
docker ps [-f|--filter] "status=status"
```

### Filter containers that mount a specific volume or have a volume mounted in a specific path

```bash
docker ps [-f|--filter] "volume=path/to/directory" --format "table .ID\t.Image\t.Names\t.Mounts"
```
