# docker-secret

> Manage Docker swarm secrets. More information: <https://docs.docker.com/reference/cli/docker/secret/>.

## Examples

### Create a new secret from `stdin`

```bash
command | docker secret create secret_name -
```

### Create a new secret from a file

```bash
docker secret create secret_name path/to/file
```

### List all secrets

```bash
docker secret ls
```

### Display detailed information on one or multiple secrets in a human friendly format

```bash
docker secret inspect --pretty secret_name1 secret_name2 ...
```

### Remove one or more secrets

```bash
docker secret rm secret_name1 secret_name2 ...
```
