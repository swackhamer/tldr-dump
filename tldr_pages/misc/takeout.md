# takeout

> A Docker-based development-only dependency manager. More information: <https://github.com/tighten/takeout>.

## Examples

### Display a list of available services

```bash
takeout enable
```

### Enable a specific service

```bash
takeout enable name
```

### Enable a specific service with the default parameters

```bash
takeout enable --default name
```

### Display a list of enabled services

```bash
takeout disable
```

### Disable a specific service

```bash
takeout disable name
```

### Disable all services

```bash
takeout disable --all
```

### Start a specific container

```bash
takeout start container_id
```

### Stop a specific container

```bash
takeout stop container_id
```
