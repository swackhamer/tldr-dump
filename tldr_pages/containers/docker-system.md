# docker-system

> Manage Docker data and display system-wide information. More information: <https://docs.docker.com/reference/cli/docker/system/>.

## Examples

### Display help

```bash
docker system
```

### Show Docker disk usage

```bash
docker system df
```

### Show detailed information on disk usage

```bash
docker system df [-v|--verbose]
```

### Remove unused data (append `--volumes` to remove unused volumes as well)

```bash
docker system prune
```

### Remove unused data created more than a specified amount of time in the past

```bash
docker system prune --filter "until=hourshminutesm"
```

### Display real-time events from the Docker daemon

```bash
docker system events
```

### Display real-time events from containers streamed as valid JSON Lines

```bash
docker system events [-f|--filter] 'type=container' --format 'json .'
```

### Display system-wide information

```bash
docker system info
```
