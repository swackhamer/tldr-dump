# waitress-serve

> Pure Python WSGI HTTP Server. More information: <https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html>.

## Examples

### Run a Python web app

```bash
waitress-serve import.path:wsgi_func
```

### Listen on port 8080 on localhost

```bash
waitress-serve --listen=localhost:8080 import.path:wsgi_func
```

### Start waitress on a Unix socket

```bash
waitress-serve --unix-socket=path/to/socket import.path:wsgi_func
```

### Use 4 threads to process requests

```bash
waitress-serve --threads=4 import.path:wsgifunc
```

### Call a factory method that returns a WSGI object

```bash
waitress-serve --call import.path.wsgi_factory
```

### Use the HTTPS URL scheme

```bash
waitress-serve --url-scheme=https import.path:wsgi_func
```
