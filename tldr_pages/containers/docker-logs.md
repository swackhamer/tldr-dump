# docker-logs

> Print container logs. More information: <https://docs.docker.com/reference/cli/docker/container/logs/>.

## Examples

### Print logs from a container

```bash
docker logs container_name
```

### Print logs and follow them

```bash
docker logs [-f|--follow] container_name
```

### Print last 5 lines

```bash
docker logs container_name [-n|--tail] 5
```

### Print logs and append them with timestamps

```bash
docker logs [-t|--timestamps] container_name
```

### Print logs from a certain point in time of container execution (i.e. 23m, 10s, 2013-01-02T13:23:37)

```bash
docker logs container_name --until time
```
