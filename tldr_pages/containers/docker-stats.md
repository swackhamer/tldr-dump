# docker-stats

> Display a live stream of resource usage statistics for containers. More information: <https://docs.docker.com/reference/cli/docker/container/stats/>.

## Examples

### Display a live stream for the statistics of all running containers

```bash
docker stats
```

### Display a live stream of statistics for one or more containers

```bash
docker stats container1 container2 ...
```

### Change the columns format to display container's CPU usage percentage

```bash
docker stats --format ".Name:\t.CPUPerc"
```

### Display statistics for all containers (both running and stopped)

```bash
docker stats [-a|--all]
```

### Disable streaming stats and only pull the current stats

```bash
docker stats --no-stream
```
