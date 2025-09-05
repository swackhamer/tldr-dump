# hugo-server

> Build and serve a site with Hugo's built-in webserver. More information: <https://gohugo.io/commands/hugo_server/>.

## Examples

### Build and serve a site

```bash
hugo server
```

### Build and serve a site on a specified port number

```bash
hugo server [-p|--port] port_number
```

### Build and serve a site while minifying supported output formats (HTML, XML, etc.)

```bash
hugo server --minify
```

### Build and serve a site in the production environment with full re-renders while minifying supported formats

```bash
hugo server [-e|--environment] production --disableFastRender --minify
```

### Display help

```bash
hugo server [-h|--help]
```
