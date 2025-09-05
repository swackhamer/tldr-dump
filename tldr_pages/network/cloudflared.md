# cloudflared

> Create a persistent connection to the Cloudflare network. More information: <https://developers.cloudflare.com/argo-tunnel/>.

## Examples

### Authenticate and associate the connection to a domain in the Cloudflare account

```bash
cloudflared tunnel login
```

### Create a tunnel with a specific name

```bash
cloudflared tunnel create name
```

### Establish a tunnel to a host in Cloudflare from the local server

```bash
cloudflared tunnel --hostname hostname localhost:port_number
```

### Establish a tunnel to a host in Cloudflare from the local server, without verifying the local server's certificate

```bash
cloudflared tunnel --hostname hostname localhost:port_number --no-tls-verify
```

### Save logs to a file

```bash
cloudflared tunnel --hostname hostname http://localhost:port_number --loglevel panic|fatal|error|warn|info|debug --logfile path/to/file
```

### Install cloudflared as a system service

```bash
cloudflared service install
```
