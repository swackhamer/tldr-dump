# httping

> Measure the latency and throughput of a web server. More information: <https://manned.org/httping>.

## Examples

### Ping the specified URL

```bash
httping -g url
```

### Ping the web server on `host` and `port`

```bash
httping -h host -p port
```

### Ping the web server on `host` using a TLS connection

```bash
httping -l -g https://host
```

### Ping the web server on `host` using HTTP basic authentication

```bash
httping -g http://host -U username -P password
```
