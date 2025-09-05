# ngrok

> Reverse proxy that creates a secure tunnel from a public endpoint to a locally running web service. More information: <https://ngrok.com>.

## Examples

### Expose a local HTTP service on a given port

```bash
ngrok http 80
```

### Expose a local HTTP service on a specific host

```bash
ngrok http foo.dev:80
```

### Expose a local HTTPS server

```bash
ngrok http https://localhost
```

### Expose TCP traffic on a given port

```bash
ngrok tcp 22
```

### Expose TLS traffic for a specific host and port

```bash
ngrok tls -hostname=example.com 443
```
