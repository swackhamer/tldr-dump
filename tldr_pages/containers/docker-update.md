# docker-update

> Update configuration of Docker containers. This command is not supported for Windows containers. More information: <https://docs.docker.com/reference/cli/docker/container/update/>.

## Examples

### Update restart policy to apply when a specific container exits

```bash
docker update --restart=always|no|on-failure|unless-stopped container_name
```

### Update the policy to restart up to three times a specific container when it exits with non-zero exit status

```bash
docker update --restart=on-failure:3 container_name
```

### Update the number of CPUs available to a specific container

```bash
docker update --cpus count container_name
```

### Update the memory limit in [M]egabytes for a specific container

```bash
docker update [-m|--memory] limitM container_name
```

### Update the maximum number of process IDs allowed inside a specific container (use `-1` for unlimited)

```bash
docker update --pids-limit count container_name
```

### Update the amount of memory in [M]egabytes a specific container can swap to disk (use `-1` for unlimited)

```bash
docker update --memory-swap limitM container_name
```
