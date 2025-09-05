# redis-server

> Persistent key-value database. More information: <https://redis.io>.

## Examples

### Start Redis server, using the default port (6379), and write logs to `stdout`

```bash
redis-server
```

### Start Redis server, using the default port, as a background process

```bash
redis-server --daemonize yes
```

### Start Redis server, using the specified port, as a background process

```bash
redis-server --port port --daemonize yes
```

### Start Redis server with a custom configuration file

```bash
redis-server path/to/redis.conf
```

### Start Redis server with verbose logging

```bash
redis-server --loglevel warning|notice|verbose|debug
```
