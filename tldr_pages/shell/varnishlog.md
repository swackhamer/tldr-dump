# varnishlog

> Display Varnish logs. More information: <https://varnish-cache.org/docs/trunk/reference/varnishlog.html>.

## Examples

### Display logs in real time

```bash
varnishlog
```

### Only display requests to a specific domain

```bash
varnishlog -q 'ReqHeader eq "Host: example.com"'
```

### Only display POST requests

```bash
varnishlog -q 'ReqMethod eq "POST"'
```

### Only display requests to a specific path

```bash
varnishlog -q 'ReqURL eq "/path"'
```

### Only display requests to paths matching a `regex`

```bash
varnishlog -q 'ReqURL ~ "regex"'
```
