# arthas

> Java diagnostic tool. See also: `arthas-watch`, `arthas-trace`. More information: <https://arthas.aliyun.com/en/>.

## Examples

### Start Arthas

```bash
java -jar path/to/arthas-boot.jar
```

### Reconnect Arthas (default port used by Arthas is 3658)

```bash
telnet localhost port_number
```

### Exit the current Arthas client without affecting other clients. equals `exit`、`logout`、`q` command

```bash
exit|quit|logout|q
```

### Terminate the Arthas server, all the Arthas clients connecting to this server will be disconnected

```bash
stop
```
