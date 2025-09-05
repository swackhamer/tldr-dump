# docker-login

> Log into a Docker registry. More information: <https://docs.docker.com/reference/cli/docker/login/>.

## Examples

### Interactively log into a registry

```bash
docker login
```

### Log into a registry with a specific username (user will be prompted for a password)

```bash
docker login [-u|--username] username
```

### Log into a registry with username and password

```bash
docker login [-u|--username] username [-p|--password] password server
```

### Log into a registry with password from `stdin`

```bash
echo "password" | docker login [-u|--username] username --password-stdin
```
