# redis-cli

> Opens a connection to a Redis server. More information: <https://redis.io/topics/rediscli>.

## Examples

### Connect to the local server

```bash
redis-cli
```

### Connect to a remote server on the default port (6379)

```bash
redis-cli -h host
```

### Connect to a remote server specifying a port number

```bash
redis-cli -h host -p port
```

### Connect to a remote server specifying a URI

```bash
redis-cli -u uri
```

### Specify a password

```bash
redis-cli -a password
```

### Execute Redis command

```bash
redis-cli redis_command
```

### Connect to the local cluster

```bash
redis-cli -c
```
