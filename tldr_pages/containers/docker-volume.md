# docker-volume

> Manage Docker volumes. More information: <https://docs.docker.com/reference/cli/docker/volume/>.

## Examples

### Create a volume

```bash
docker volume create volume_name
```

### Create a volume with a specific label

```bash
docker volume create --label label volume_name
```

### Create a `tmpfs` volume a size of 100 MiB and an uid of 1000

```bash
docker volume create [-o|--opt] type=tmpfs [-o|--opt] device=tmpfs [-o|--opt] o=size=100m,uid=1000 volume_name
```

### List all volumes

```bash
docker volume ls
```

### Remove a volume

```bash
docker volume rm volume_name
```

### Display information about a volume

```bash
docker volume inspect volume_name
```

### Remove all unused local volumes

```bash
docker volume prune
```

### Display help for a subcommand

```bash
docker volume subcommand --help
```
