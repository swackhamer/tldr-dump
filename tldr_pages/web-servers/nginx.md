# nginx

> Nginx web server. More information: <https://nginx.org/en/>.

## Examples

### Start server with the default configuration file

```bash
nginx
```

### Start server with a custom configuration file

```bash
nginx -c configuration_file
```

### Start server with a prefix for all relative paths in the configuration file

```bash
nginx -c configuration_file -p prefix/for/relative/paths
```

### Test the configuration without affecting the running server

```bash
nginx -t
```

### Reload the configuration by sending a signal with no downtime

```bash
nginx -s reload
```
