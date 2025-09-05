# docker-exec

> Execute a command on an already running Docker container. More information: <https://docs.docker.com/reference/cli/docker/container/exec/>.

## Examples

### Enter an interactive shell session on an already-running container

```bash
docker exec [-it|--interactive --tty] container_name /bin/bash
```

### Run a command in the background (detached) on a running container

```bash
docker exec [-d|--detach] container_name command
```

### Select the working directory for a given command to execute into

```bash
docker exec [-it|--interactive --tty] [-w|--workdir] path/to/directory container_name command
```

### Run a command in background on existing container but keep `stdin` open

```bash
docker exec [-i|--interactive] [-d|--detach] container_name command
```

### Set an environment variable in a running Bash session

```bash
docker exec [-it|--interactive --tty] [-e|--env] variable_name=value container_name /bin/bash
```

### Run a command as a specific user

```bash
docker exec [-u|--user] user container_name command
```
