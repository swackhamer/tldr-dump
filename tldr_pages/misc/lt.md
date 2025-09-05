# lt

> Localtunnel exposes your localhost to the world for easy testing and sharing. More information: <https://github.com/localtunnel/localtunnel>.

## Examples

### Start tunnel from a specific port

```bash
lt [-p|--port] 8000
```

### Specify the upstream server doing the forwarding

```bash
lt [-p|--port] 8000 [-h|--host] host
```

### Request a specific subdomain

```bash
lt [-p|--port] 8000 [-s|--subdomain] subdomain
```

### Print basic request info

```bash
lt [-p|--port] 8000 --print-requests
```

### Open the tunnel URL in the default web browser

```bash
lt [-p|--port] 8000 [-o|--open]
```
