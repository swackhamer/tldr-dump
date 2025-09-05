# gixy

> Analyze nginx configuration files. More information: <https://github.com/yandex/gixy>.

## Examples

### Analyze nginx configuration (default path: `/etc/nginx/nginx.conf`)

```bash
gixy
```

### Analyze nginx configuration but skip specific tests

```bash
gixy --skips http_splitting
```

### Analyze nginx configuration with the specific severity level

```bash
gixy -l|-ll|-lll
```

### Analyze nginx configuration files on the specific path

```bash
gixy path/to/configuration_file_1 path/to/configuration_file_2
```
