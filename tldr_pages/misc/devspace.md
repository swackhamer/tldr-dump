# devspace

> Develop, deploy, and debug applications inside Kubernetes. More information: <https://devspace.sh/docs/cli>.

## Examples

### Initialize a new DevSpace project in the current directory

```bash
devspace init
```

### Start development mode with port forwarding, file synchronization, and terminal access

```bash
devspace dev
```

### Start development mode in a specific namespace

```bash
devspace dev [-n|--namespace] namespace
```

### Deploy the project to Kubernetes

```bash
devspace deploy
```

### Deploy the project with a specific profile

```bash
devspace deploy [-p|--profile] profile-name
```

### Build all defined images

```bash
devspace build
```

### Follow logs from a pod

```bash
devspace logs [-f|--follow]
```

### Open the DevSpace UI in the browser

```bash
devspace ui
```
