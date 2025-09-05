# mitmweb

> A web-based interactive man-in-the-middle HTTP proxy. See also: `mitmproxy`. More information: <https://docs.mitmproxy.org/stable/concepts-options>.

## Examples

### Start `mitmweb` with default settings

```bash
mitmweb
```

### Start `mitmweb` bound to a custom address and port

```bash
mitmweb --listen-host ip_address --listen-port port
```

### Start `mitmweb` using a script to process traffic

```bash
mitmweb --scripts path/to/script.py
```
