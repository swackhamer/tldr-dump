# live-server

> A simple development HTTP server with live reload capability. More information: <https://github.com/tapio/live-server>.

## Examples

### Serve an `index.html` file and reload on changes

```bash
live-server
```

### Specify a port (default is 8080) from which to serve a file

```bash
live-server --port=8081
```

### Specify a given file to serve

```bash
live-server --open=about.html
```

### Proxy all requests for ROUTE to URL

```bash
live-server --proxy=/:http:localhost:3000
```
