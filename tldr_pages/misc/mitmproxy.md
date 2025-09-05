# mitmproxy

> An interactive man-in-the-middle HTTP proxy. See also: `mitmweb`, `mitmdump`. More information: <https://docs.mitmproxy.org/stable/>.

## Examples

### Start `mitmproxy` with default settings (will listen on port `8080`)

```bash
mitmproxy
```

### Start `mitmproxy` bound to a custom address and port

```bash
mitmproxy --listen-host ip_address [-p|--listen-port] port
```

### Start `mitmproxy` using a script to process traffic

```bash
mitmproxy [-s|--scripts] path/to/script.py
```

### Export the logs with SSL/TLS master keys to external programs (wireshark, etc.)

```bash
SSLKEYLOGFILE="path/to/file" mitmproxy
```

### Specify mode of operation of the proxy server (`regular` is the default)

```bash
mitmproxy [-m|--mode] regular|transparent|socks5|...
```

### Set the console layout

```bash
mitmproxy --console-layout horizontal|single|vertical
```

### Save all proxied traffic to a file for later analysis

```bash
mitmproxy [-w|--save-stream-file] path/to/dump.mitm
```

### Replay a previously saved HTTP flow file

```bash
mitmproxy [-nr|--no-server --rfile] path/to/dump.mitm
```
