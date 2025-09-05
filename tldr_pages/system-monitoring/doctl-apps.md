# doctl-apps

> Manage DigitalOcean apps. More information: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

## Examples

### Create an app

```bash
doctl [a|apps] [c|create]
```

### Create a deployment for a specific app

```bash
doctl [a|apps] [cd|create-deployment] app_id
```

### Delete an app interactively

```bash
doctl [a|apps] [d|delete] app_id
```

### Get an app

```bash
doctl [a|apps] [g|get]
```

### List all apps

```bash
doctl [a|apps] [ls|list]
```

### List all deployments from a specific app

```bash
doctl [a|apps] [lsd|list-deployments] app_id
```

### Get logs from a specific app

```bash
doctl [a|apps] [l|logs] app_id
```

### Update a specific app with a given app spec

```bash
doctl [a|apps] [u|update] app_id --spec path/to/spec.yml
```
