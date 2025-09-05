# caddy

> An enterprise-ready open source web server with automatic HTTPS, written in Go. More information: <https://caddyserver.com>.

## Examples

### Start Caddy in the foreground

```bash
caddy run
```

### Start Caddy with the specified Caddyfile

```bash
caddy run --config path/to/Caddyfile
```

### Start Caddy in the background

```bash
caddy start
```

### Stop a background Caddy process

```bash
caddy stop
```

### Run a simple file server on the specified port with a browsable interface

```bash
caddy file-server --listen :8000 --browse
```

### Run a reverse proxy server

```bash
caddy reverse-proxy --from :80 --to localhost:8000
```
