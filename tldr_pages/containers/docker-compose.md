# docker-compose

> Run and manage multi container Docker applications. More information: <https://docs.docker.com/reference/cli/docker/compose/>.

## Examples

### List all running containers

```bash
docker compose ps
```

### Create and start all containers in the background using a `docker-compose.yml` file from the current directory

```bash
docker compose up [-d|--detach]
```

### Start all containers, rebuild if necessary

```bash
docker compose up --build
```

### Start all containers by specifying a project name and using an alternate compose file

```bash
docker compose [-p|--project-name] project_name [-f|--file] path/to/file up
```

### Stop all running containers

```bash
docker compose stop
```

### Stop and remove all containers, networks, images, and volumes

```bash
docker compose down --rmi all [-v|--volumes]
```

### Follow logs for all containers

```bash
docker compose logs [-f|--follow]
```

### Follow logs for a specific container

```bash
docker compose logs [-f|--follow] container_name
```
