# flyctl

> Tool for flyctl.io. More information: <https://github.com/superfly/flyctl>.

## Examples

### Sign into a Fly account

```bash
flyctl auth login
```

### Launch an application from a specific Dockerfile (the default path is the current working directory)

```bash
flyctl launch --dockerfile path/to/dockerfile
```

### Open the current deployed application in the default web browser

```bash
flyctl open
```

### Deploy the Fly applications from a specific Dockerfile

```bash
flyctl deploy --dockerfile path/to/dockerfile
```

### Open the Fly Web UI for the current application in a web browser

```bash
flyctl dashboard
```

### List all applications in the logged-in Fly account

```bash
flyctl apps list
```

### View the status of a specific running application

```bash
flyctl status --app app_name
```

### Display version information

```bash
flyctl version
```
