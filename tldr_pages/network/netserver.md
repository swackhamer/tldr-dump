# netserver

> Server-side command for `netperf`, the benchmarking application that measures network throughput. See also: `netperf` for the client-side command. More information: <https://manned.org/netserver.1>.

## Examples

### Start a server on the default port (12865) and fork to background

```bash
netserver
```

### Start server in foreground and do not fork

```bash
netserver -D
```

### Specify [p]ort

```bash
netserver -p port
```

### Force IPv[4] or IPv[6]

```bash
netserver -4|6
```
