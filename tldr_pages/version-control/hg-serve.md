# hg-serve

> Start a standalone Mercurial web server for browsing repositories. More information: <https://www.mercurial-scm.org/help/commands/serve>.

## Examples

### Start a web server instance

```bash
hg serve
```

### Start a web server instance on the specified port

```bash
hg serve [-p|--port] port
```

### Start a web server instance on the specified listening address

```bash
hg serve [-a|--address] address
```

### Start a web server instance with a specific identifier

```bash
hg serve [-n|--name] name
```

### Start a web server instance using the specified theme (see the templates directory)

```bash
hg serve --style style
```

### Start a web server instance using the specified SSL certificate bundle

```bash
hg serve --certificate path/to/certificate
```
