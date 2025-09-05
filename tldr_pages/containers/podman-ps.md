# podman-ps

> List Podman containers. More information: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

## Examples

### List currently running Podman containers

```bash
podman ps
```

### List all Podman containers (running and stopped)

```bash
podman ps --all
```

### Show the latest created container (includes all states)

```bash
podman ps --latest
```

### Filter containers that contain a substring in their name

```bash
podman ps --filter "name=name"
```

### Filter containers that share a given image as an ancestor

```bash
podman ps --filter "ancestor=image:tag"
```

### Filter containers by exit status code

```bash
podman ps --all --filter "exited=code"
```

### Filter containers by status (created, running, removing, paused, exited and dead)

```bash
podman ps --filter "status=status"
```

### Filter containers that mount a specific volume or have a volume mounted in a specific path

```bash
podman ps --filter "volume=path/to/directory" --format "table .ID\t.Image\t.Names\t.Mounts"
```
