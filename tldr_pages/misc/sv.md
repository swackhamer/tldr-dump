# sv

> Control a running runsv service. More information: <https://manned.org/sv.8>.

## Examples

### Start a service

```bash
sudo sv up path/to/service
```

### Stop a service

```bash
sudo sv down path/to/service
```

### Get service status

```bash
sudo sv status path/to/service
```

### Reload a service

```bash
sudo sv reload path/to/service
```

### Start a service, but only if it's not running and don't restart it if it stops

```bash
sudo sv once path/to/service
```
