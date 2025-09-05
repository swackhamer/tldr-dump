# mitmdump

> View, record, and programmatically transform HTTP traffic. The command-line counterpart to mitmproxy. More information: <https://docs.mitmproxy.org/stable/#mitmdump>.

## Examples

### Start a proxy and save all output to a file

```bash
mitmdump [-w|--wfile] path/to/file
```

### Filter a saved traffic file to just POST requests

```bash
mitmdump [-nr|--no-server --read-flows] input_filename [-w|--wfile] output_filename "~m post"
```

### Replay a saved traffic file

```bash
mitmdump [-nc|--no-server --client-replay] path/to/file
```

### Intercept DNS traffic (starts an intercepting DNS server on 127.0.0.1:53)

```bash
sudo mitmdump [-m|--mode] dns
```
